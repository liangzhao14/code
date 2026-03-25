/**
 * 新闻数据模块
 * 基于RSS订阅获取真实新闻
 */

const NewsData = {
    // RSS2JSON API 地址
    RSS2JSON_API: 'https://api.rss2json.com/v1/api.json?rss_url=',

    // 北京新闻RSS源
    beijingSources: [
        { name: '新华网', url: 'http://www.xinhuanet.com/politics/news_politics.xml', category: '政治' },
        { name: '人民网', url: 'http://news.people.com.cn/RSS/politics.xml', category: '政治' },
        { name: '央视新闻', url: 'https://news.cctv.com/RSS/politics.xml', category: '政治' },
        { name: '中国青年报', url: 'https://news.cyol.com/gb/dykb/index.xml', category: '民生' },
        { name: '新京报', url: 'https://www.bjnews.com.cn/feed', category: '综合' }
    ],

    // AI科技新闻RSS源
    aiSources: [
        { name: 'TechCrunch', url: 'https://techcrunch.com/feed/', category: '国际' },
        { name: 'The Verge', url: 'https://www.theverge.com/rss/index.xml', category: '国际' },
        { name: 'Wired', url: 'https://www.wired.com/feed/rss', category: '国际' },
        { name: 'MIT Tech Review', url: 'https://www.technologyreview.com/feed/', category: '国际' },
        { name: '36Kr', url: 'https://www.36kr.com/feed/', category: '国内' },
        { name: '爱范儿', url: 'https://www.ifanr.com/feed/', category: '国内' }
    ],

    // 缓存
    cache: {},
    cacheExpiry: 5 * 60 * 1000, // 5分钟缓存

    /**
     * 获取RSS源数据
     * @param {string} url - RSS源URL
     * @returns {Promise<Array>} 新闻列表
     */
    fetchRSS: async function(url) {
        const cacheKey = url;
        const now = Date.now();

        // 检查缓存
        if (this.cache[cacheKey] && (now - this.cache[cacheKey].time < this.cacheExpiry)) {
            return this.cache[cacheKey].data;
        }

        try {
            const response = await fetch(this.RSS2JSON_API + encodeURIComponent(url));
            const data = await response.json();

            if (data.status === 'ok' && data.items) {
                // 缓存结果
                this.cache[cacheKey] = {
                    time: now,
                    data: data.items
                };
                return data.items;
            }
            return [];
        } catch (error) {
            console.error('获取RSS失败:', url, error);
            return [];
        }
    },

    /**
     * 将 Date 对象格式化为 YYYY-MM-DD 字符串
     */
    formatDateStr: function(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    },

    /**
     * 获取北京新闻
     * @param {string|null} dateFilter - 按日期过滤（YYYY-MM-DD），null 表示不过滤
     * @returns {Promise<Array>} 北京新闻列表
     */
    getBeijingNews: async function(dateFilter) {
        const allNews = [];

        // 并行获取所有RSS源
        const promises = this.beijingSources.map(async (source) => {
            const items = await this.fetchRSS(source.url);
            let candidates = items;
            if (dateFilter) {
                candidates = items.filter(item => {
                    if (!item.pubDate) return false;
                    try { return this.formatDateStr(new Date(item.pubDate)) === dateFilter; }
                    catch { return false; }
                });
            }
            return candidates.slice(0, 3).map(item => ({
                id: this.generateId(),
                title: this.cleanTitle(item.title),
                desc: this.cleanDesc(item.description),
                source: source.name,
                category: source.category,
                time: this.formatRSSDate(item.pubDate),
                url: item.link
            }));
        });

        const results = await Promise.all(promises);
        results.forEach(items => allNews.push(...items));

        // 按时间排序
        allNews.sort((a, b) => new Date(b.time) - new Date(a.time));

        return allNews.slice(0, 10);
    },

    /**
     * 获取AI新闻
     * @param {string|null} dateFilter - 按日期过滤（YYYY-MM-DD），null 表示不过滤
     * @returns {Promise<Array>} AI新闻列表
     */
    getAINews: async function(dateFilter) {
        const allNews = [];

        const promises = this.aiSources.map(async (source) => {
            const items = await this.fetchRSS(source.url);
            let candidates = items;
            if (dateFilter) {
                candidates = items.filter(item => {
                    if (!item.pubDate) return false;
                    try { return this.formatDateStr(new Date(item.pubDate)) === dateFilter; }
                    catch { return false; }
                });
            }
            return candidates.slice(0, 3).map(item => ({
                id: this.generateId(),
                title: this.cleanTitle(item.title),
                desc: this.cleanDesc(item.description),
                source: source.name,
                category: source.category,
                time: this.formatRSSDate(item.pubDate),
                url: item.link
            }));
        });

        const results = await Promise.all(promises);
        results.forEach(items => allNews.push(...items));

        // 按时间排序
        allNews.sort((a, b) => new Date(b.time) - new Date(a.time));

        return allNews.slice(0, 10);
    },

    /**
     * 获取指定日期的新闻
     * 今日：不过滤，返回 RSS 最新内容
     * 历史日期：按 pubDate 过滤，无结果则返回空列表
     * @param {string} dateStr - 日期字符串 (YYYY-MM-DD)
     * @returns {Promise<Object>} 包含北京新闻和AI新闻的对象
     */
    getNewsByDate: async function(dateStr) {
        const cacheKey = 'date-' + dateStr;
        const now = Date.now();

        if (this.cache[cacheKey] && (now - this.cache[cacheKey].time < this.cacheExpiry)) {
            return this.cache[cacheKey].data;
        }

        const todayStr = this.formatDateStr(new Date());
        const isToday = dateStr === todayStr;
        // 今日不过滤（RSS 实时内容），历史日期按日期过滤
        const dateFilter = isToday ? null : dateStr;

        const [beijing, ai] = await Promise.all([
            this.getBeijingNews(dateFilter),
            this.getAINews(dateFilter)
        ]);

        const result = {
            beijing: beijing,
            ai: ai,
            date: dateStr,
            isToday: isToday
        };

        this.cache[cacheKey] = { time: now, data: result };

        return result;
    },

    /**
     * 清理标题（去除HTML实体等）
     */
    cleanTitle: function(title) {
        if (!title) return '无标题';
        return title
            .replace(/&amp;/g, '&')
            .replace(/&lt;/g, '<')
            .replace(/&gt;/g, '>')
            .replace(/&quot;/g, '"')
            .replace(/&#039;/g, "'")
            .replace(/\s+/g, ' ')
            .trim();
    },

    /**
     * 清理描述（提取纯文本）
     */
    cleanDesc: function(desc) {
        if (!desc) return '';
        // 去除HTML标签
        let text = desc.replace(/<[^>]+>/g, '');
        // 清理HTML实体
        text = text
            .replace(/&amp;/g, '&')
            .replace(/&lt;/g, '<')
            .replace(/&gt;/g, '>')
            .replace(/&quot;/g, '"')
            .replace(/&#039;/g, "'")
            .replace(/&nbsp;/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
        // 截取前100字
        return text.length > 100 ? text.substring(0, 100) + '...' : text;
    },

    /**
     * 格式化RSS日期
     */
    formatRSSDate: function(dateStr) {
        if (!dateStr) return '';
        try {
            const date = new Date(dateStr);
            const hours = String(date.getHours()).padStart(2, '0');
            const minutes = String(date.getMinutes()).padStart(2, '0');
            return `${hours}:${minutes}`;
        } catch {
            return '';
        }
    },

    /**
     * 生成唯一ID
     */
    generateId: function() {
        return 'news-' + Math.random().toString(36).substr(2, 9);
    },

    /**
     * 清除缓存
     */
    clearCache: function() {
        this.cache = {};
    }
};

// 导出模块
if (typeof module !== 'undefined' && module.exports) {
    module.exports = NewsData;
}
