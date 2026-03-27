"""生成XMind脑图：项目组织分工与实施保障"""
import json
import zipfile
import os

content = [
    {
        "id": "root",
        "class": "sheet",
        "title": "项目组织分工与实施保障",
        "rootTopic": {
            "id": "t0",
            "class": "topic",
            "title": "项目组织架构\n（14~18人）",
            "structureClass": "org.xmind.ui.map.clockwise",
            "children": {
                "attached": [
                    {
                        "id": "t1",
                        "title": "项目负责人（1人）",
                        "labels": ["统筹决策"],
                        "children": {
                            "attached": [
                                {"id": "t1a", "title": "统筹推进整体治理工作"},
                                {"id": "t1b", "title": "组织重要事项决策"},
                                {"id": "t1c", "title": "资源协调"},
                            ]
                        }
                    },
                    {
                        "id": "t2",
                        "title": "业务负责人/甲方（1人）",
                        "labels": ["业务口径"],
                        "children": {
                            "attached": [
                                {"id": "t2a", "title": "明确业务场景和专业口径"},
                                {"id": "t2b", "title": "提供KRT系统数据"},
                                {"id": "t2c", "title": "审核内容准确性"},
                            ]
                        }
                    },
                    {
                        "id": "t3",
                        "title": "数据工程师（2人）",
                        "labels": ["数据治理"],
                        "children": {
                            "attached": [
                                {"id": "t3a", "title": "数据采集"},
                                {"id": "t3b", "title": "数据清洗与脱敏"},
                                {"id": "t3c", "title": "数据增强处理"},
                            ]
                        }
                    },
                    {
                        "id": "t4",
                        "title": "标注负责人（1人）",
                        "labels": ["标注管理"],
                        "children": {
                            "attached": [
                                {"id": "t4a", "title": "试标与批量标注组织"},
                                {"id": "t4b", "title": "口径统一管理"},
                                {"id": "t4c", "title": "标注人员资质考核"},
                            ]
                        }
                    },
                    {
                        "id": "t5",
                        "title": "标注业务人员（6~10人）",
                        "labels": ["核心产能"],
                        "children": {
                            "attached": [
                                {"id": "t5a", "title": "执行批量数据标注"},
                                {"id": "t5b", "title": "按口径规范操作"},
                            ]
                        }
                    },
                    {
                        "id": "t6",
                        "title": "质检人员（2人）",
                        "labels": ["质量保障"],
                        "children": {
                            "attached": [
                                {"id": "t6a", "title": "三级质检组织执行"},
                                {"id": "t6b", "title": "质检记录管理"},
                                {"id": "t6c", "title": "整改台账管理"},
                            ]
                        }
                    },
                    {
                        "id": "t7",
                        "title": "核电领域专家终审（1人）",
                        "labels": ["终审裁定"],
                        "children": {
                            "attached": [
                                {"id": "t7a", "title": "安全类/高难度数据终审"},
                                {"id": "t7b", "title": "标注标准修订"},
                                {"id": "t7c", "title": "争议裁定"},
                            ]
                        }
                    },
                    {
                        "id": "t8",
                        "title": "技术支持人员（1人）",
                        "labels": ["环境保障"],
                        "children": {
                            "attached": [
                                {"id": "t8a", "title": "平台与工具保障"},
                                {"id": "t8b", "title": "提交环境维护"},
                            ]
                        }
                    },
                    {
                        "id": "t9",
                        "title": "安全与场地要求",
                        "labels": ["合规管控"],
                        "children": {
                            "attached": [
                                {"id": "t9a", "title": "标注场地需门禁系统"},
                                {"id": "t9b", "title": "涉密数据内网标注"},
                                {"id": "t9c", "title": "工具须操作留痕"},
                                {"id": "t9d", "title": "禁用境外在线工具"},
                            ]
                        }
                    },
                ]
            }
        }
    }
]

metadata = {
    "creator": {"name": "XMind", "version": "12.0.0"}
}

manifest = {
    "file-entries": {
        "content.json": {},
        "metadata.json": {}
    }
}

out_path = os.path.join(os.path.dirname(__file__), '项目组织分工与实施保障.xmind')

with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('content.json', json.dumps(content, ensure_ascii=False, indent=2))
    zf.writestr('metadata.json', json.dumps(metadata, ensure_ascii=False, indent=2))
    zf.writestr('manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))

print(f'已生成: {out_path}')
