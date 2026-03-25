/**
 * 每日新闻查看器 - 主应用逻辑
 */

const App = {
    // DOM元素
    elements: {
        dateInput: null,
        refreshBtn: null,
        beijingNews: null,
        aiNews: null,
        beijingCount: null,
        aiCount: null,
        beijingSkeleton: null,
        aiSkeleton: null,
        beijingEmpty: null,
        aiEmpty: null,
        errorToast: null,
        errorMessage: null,
        retryBtn: null
    },

    // 当前选中的日期
    currentDate: null,

    // 加载状态
    isLoading: false,

    /**
     * 初始化应用
     */
    init: function() {
        this.cacheElements();
        this.setDefaultDate();
        this.bindEvents();
        this.loadNews();
    },

    /**
     * 缓存DOM元素
     */
    cacheElements: function() {
        this.elements = {
            dateInput: document.getElementById('news-date'),
            refreshBtn: document.getElementById('refresh-btn'),
            beijingNews: document.getElementById('beijing-news'),
            aiNews: document.getElementById('ai-news'),
            beijingCount: document.getElementById('beijing-count'),
            aiCount: document.getElementById('ai-count'),
            beijingSkeleton: document.getElementById('beijing-skeleton'),
            aiSkeleton: document.getElementById('ai-skeleton'),
            beijingEmpty: document.getElementById('beijing-empty'),
            aiEmpty: document.getElementById('ai-empty'),
            errorToast: document.getElementById('error-toast'),
            errorMessage: document.querySelector('.error-message'),
            retryBtn: document.getElementById('retry-btn')
        };
    },

    /**
     * 设置默认日期
     */
    setDefaultDate: function() {
        const today = new Date();
        const dateStr = this.formatDate(today);
        this.currentDate = dateStr;
        this.elements.dateInput.value = dateStr;

        // RSS是实时获取的，日期选择保留但主要显示当天
        // 可以选择过去30天的日期
        const monthAgo = new Date(today);
        monthAgo.setDate(monthAgo.getDate() - 30);
        this.elements.dateInput.min = this.formatDate(monthAgo);
        this.elements.dateInput.max = dateStr;
    },

    /**
     * 格式化日期为YYYY-MM-DD
     */
    formatDate: function(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    },

    /**
     * 绑定事件
     */
    bindEvents: function() {
        // 日期变化事件
        this.elements.dateInput.addEventListener('change', (e) => {
            this.currentDate = e.target.value;
            this.loadNews();
        });

        // 刷新按钮
        this.elements.refreshBtn.addEventListener('click', () => {
            this.loadNews();
        });

        // 重试按钮
        this.elements.retryBtn.addEventListener('click', () => {
            this.hideError();
            this.loadNews();
        });
    },

    /**
     * 加载新闻（异步）
     */
    loadNews: async function() {
        if (this.isLoading) return;

        this.isLoading = true;
        this.showLoading();

        try {
            const newsData = await NewsData.getNewsByDate(this.currentDate);
            this.renderNews(newsData);
            this.hideError();
        } catch (error) {
            console.error('加载新闻失败:', error);
            this.showError('加载新闻失败，请检查网络后重试');
        } finally {
            this.isLoading = false;
            this.hideLoading();
        }
    },

    /**
     * 显示加载状态
     */
    showLoading: function() {
        this.elements.refreshBtn.classList.add('loading');
        this.elements.beijingSkeleton.style.display = 'flex';
        this.elements.aiSkeleton.style.display = 'flex';
        this.elements.beijingNews.innerHTML = '';
        this.elements.aiNews.innerHTML = '';
        this.elements.beijingEmpty.style.display = 'none';
        this.elements.aiEmpty.style.display = 'none';
    },

    /**
     * 隐藏加载状态
     */
    hideLoading: function() {
        this.elements.refreshBtn.classList.remove('loading');
        this.elements.beijingSkeleton.style.display = 'none';
        this.elements.aiSkeleton.style.display = 'none';
    },

    /**
     * 渲染新闻
     */
    renderNews: function(data) {
        // 渲染北京新闻
        if (data.beijing.length > 0) {
            this.elements.beijingNews.innerHTML = data.beijing
                .map(news => this.createNewsCard(news, 'beijing'))
                .join('');
            this.elements.beijingCount.textContent = `${data.beijing.length} 条`;
            this.elements.beijingEmpty.style.display = 'none';
        } else {
            this.elements.beijingNews.innerHTML = '';
            this.elements.beijingCount.textContent = '0 条';
            this.elements.beijingEmpty.style.display = 'block';
        }

        // 渲染AI新闻
        if (data.ai.length > 0) {
            this.elements.aiNews.innerHTML = data.ai
                .map(news => this.createNewsCard(news, 'ai'))
                .join('');
            this.elements.aiCount.textContent = `${data.ai.length} 条`;
            this.elements.aiEmpty.style.display = 'none';
        } else {
            this.elements.aiNews.innerHTML = '';
            this.elements.aiCount.textContent = '0 条';
            this.elements.aiEmpty.style.display = 'block';
        }
    },

    /**
     * HTML 转义，防止 XSS
     */
    escapeHtml: function(str) {
        if (!str) return '';
        const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
        return String(str).replace(/[&<>"']/g, m => map[m]);
    },

    /**
     * URL 校验，只允许 http/https
     */
    sanitizeUrl: function(url) {
        if (!url) return '#';
        try {
            const parsed = new URL(url);
            return (parsed.protocol === 'http:' || parsed.protocol === 'https:') ? url : '#';
        } catch {
            return '#';
        }
    },

    /**
     * 创建新闻卡片HTML
     */
    createNewsCard: function(news, type) {
        const timeHtml = news.time
            ? `<span class="news-time">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                ${this.escapeHtml(news.time)}
               </span>`
            : '';

        return `
            <a href="${this.sanitizeUrl(news.url)}" class="news-card" target="_blank" rel="noopener noreferrer" data-id="${this.escapeHtml(news.id)}">
                <div class="news-meta">
                    <span class="news-source">${this.escapeHtml(news.source)}</span>
                    ${timeHtml}
                </div>
                <h3 class="news-title">${this.escapeHtml(news.title)}</h3>
                <p class="news-desc">${this.escapeHtml(news.desc)}</p>
                <div class="news-footer">
                    <span class="news-category">${this.escapeHtml(news.category)}</span>
                    <span class="news-read-more">阅读全文 →</span>
                </div>
            </a>
        `;
    },

    /**
     * 显示错误提示
     */
    showError: function(message) {
        this.elements.errorMessage.textContent = message;
        this.elements.errorToast.classList.remove('hidden');
    },

    /**
     * 隐藏错误提示
     */
    hideError: function() {
        this.elements.errorToast.classList.add('hidden');
    }
};

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    App.init();
});
