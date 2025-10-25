#!/usr/bin/env python3
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any

def load_monitoring_results() -> List[Dict[str, Any]]:
    """加载 monitoring_results.json"""
    if not os.path.exists("monitoring_results.json"):
        print("No monitoring results found")
        return []
    try:
        with open("monitoring_results.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error loading monitoring_results.json: {e}")
        return []

def get_beijing_time() -> datetime:
    """获取当前北京时间"""
    return datetime.utcnow() + timedelta(hours=8)

def format_time(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M")

def generate_report():
    """生成精简、结构化的故障聚合报告"""
    results = load_monitoring_results()
    if not results:
        return

    # 筛选失败的工作流
    failed_workflows = [r for r in results if r.get('conclusion') == 'failure']
    if not failed_workflows:
        print("No failed workflows to report")
        return

    now = get_beijing_time()
    date_str = now.strftime("%Y%m%d")  # 用于 Discussion 标题

    # 计算时间范围（基于失败运行的创建和完成时间）
    created_times = [
        datetime.fromisoformat(r["created_at"].replace("Z", "+00:00")) + timedelta(hours=8)
        for r in failed_workflows
    ]
    updated_times = [
        datetime.fromisoformat(r["updated_at"].replace("Z", "+00:00")) + timedelta(hours=8)
        for r in failed_workflows
    ]
    start_time = min(created_times)
    end_time = max(updated_times)

    total = len(results)
    failed_count = len(failed_workflows)
    success_rate = 0 if total == 0 else round((total - failed_count) / total * 100, 1)

    # === 第一行：用于 Discussion 标题提取 ===
    report = f"# {date_str} GitHub Actions 故障聚合报告\n\n"
    report += f"### 执行概览\n"
    report += f"- **监控时间范围**: {format_time(start_time)}–{format_time(end_time)} (UTC+8)\n"
    report += f"- **检测到失败运行**: {failed_count}个\n"
    report += f"- **成功率**: {success_rate}% (本批次)\n\n"
    report += f"### 故障详情\n"

    for wf in failed_workflows:
        run_id = wf.get("run_id", "N/A")
        name = wf["name"]
        html_url = wf.get("html_url", "#")
        details = wf.get("failure_details", [])

        report += f"\n**Run-{run_id}** | [{name}]({html_url})\n"

        if not details:
            report += "└─ 无失败作业详情\n"
            continue

        failed_jobs = [j for j in details if j.get("steps")]
        for i, job in enumerate(failed_jobs):
            job_name = job["name"]
            steps = job["steps"]
            prefix = "└─" if i == len(failed_jobs) - 1 else "├─"
            report += f"{prefix} **失败作业**: {job_name}\n"

            for j, step in enumerate(steps):
                step_name = step["name"]
                step_num = step["number"]
                step_prefix = "   " if j < len(steps) - 1 else "   └─"
                report += f"{step_prefix} **失败步骤**: {step_name} (Step {step_num})\n"

    # === 保存报告 ===
    try:
        with open("failure_details.md", "w", encoding="utf-8") as f:
            f.write(report.rstrip() + "\n")
        print("Report generated: failure_details.md")
        print(f"Report size: {os.path.getsize('failure_details.md')} bytes")
    except Exception as e:
        print(f"Error writing report: {e}")

if __name__ == "__main__":
    generate_report()