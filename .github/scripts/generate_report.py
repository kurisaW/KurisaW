#!/usr/bin/env python3
import json
import os
from datetime import datetime, timedelta

def generate_report():
    """生成简化的失败分析报告"""
    try:
        if not os.path.exists("monitoring_results.json"):
            print("No monitoring results found")
            return
        
        with open("monitoring_results.json", "r") as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading monitoring_results.json: {e}")
        return
    
    # 获取当前时间（UTC+8），正确处理跨天
    now = datetime.utcnow()
    beijing_time = now + timedelta(hours=8)
    date_string = beijing_time.strftime("%Y%m%d")
    time_string = beijing_time.strftime("%H:%M:%S")
    
    report = f"# **Report:** {beijing_time.strftime('%Y-%m-%d %H:%M:%S')} (UTC+8)"
    
    # 只处理失败的工作流
    failed_workflows = [r for r in results if r.get('conclusion') == 'failure']
    
    if not failed_workflows:
        report += "✅ 本次测试无失败工作流\n"
    else:
        for workflow in failed_workflows:
            report += f"### ❌ {workflow['name']}\n\n"
            report += f"**运行ID:** `{workflow.get('run_id', 'N/A')}`\n\n"
            report += f"**日志链接:** [查看完整日志]({workflow.get('html_url', '#')})\n\n"
            
            if workflow.get('failure_details'):
                report += "**失败详情:**\n\n"
                report += "```\n"
                for job in workflow['failure_details']:
                    report += f"作业失败: {job['name']}\n"
                    for step in job.get('steps', []):
                        report += f"  步骤 {step['number']}: {step['name']} - 失败\n"
                report += "```\n\n"
            else:
                report += "**失败详情:** 无详细失败信息\n\n"
            
            report += "---\n\n"
    
    # 保存报告
    try:
        with open("failure_details.md", "w", encoding="utf-8") as f:
            f.write(report)
        print("Report generated: failure_details.md")
        print(f"Report size: {os.path.getsize('failure_details.md')} bytes")
    except Exception as e:
        print(f"Error writing report: {e}")

if __name__ == "__main__":
    generate_report()