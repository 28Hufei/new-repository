"""
银行报告生成器
"""

from datetime import datetime

class ReportGenerator:
    """
    生成银行业务报告
    """
    
    def __init__(self, metrics_calculator):
        """
        初始化报告生成器
        
        Args:
            metrics_calculator: 指标计算器实例
        """
        self.calculator = metrics_calculator
        self.generated_time = None
    
    def generate_summary_report(self):
        """生成摘要报告"""
        self.generated_time = datetime.now()
        
        report = {
            'generated_at': self.generated_time.isoformat(),
            'total_balance': self.calculator.calculate_total_balance(),
            'average_balance': self.calculator.calculate_average_balance(),
            'total_transactions': self.calculator.calculate_total_transactions(),
            'total_accounts': len(self.calculator.accounts),
            'high_value_accounts': len(self.calculator.get_high_value_accounts())
        }
        
        return report
    
    def generate_detailed_report(self):
        """生成详细报告"""
        summary = self.generate_summary_report()
        summary['metrics_by_type'] = self.calculator.calculate_metrics_by_type()
        summary['high_value_accounts'] = [
            {
                'account_id': acc.account_id,
                'holder': acc.account_holder,
                'balance': acc.get_balance()
            }
            for acc in self.calculator.get_high_value_accounts()
        ]
        
        return summary
    
    def print_report(self, report):
        """打印报告"""
        print("=" * 50)
        print("银行指标报告")
        print("=" * 50)
        print(f"生成时间: {report['generated_at']}")
        print(f"总账户数: {report['total_accounts']}")
        print(f"总余额: ${report['total_balance']:.2f}")
        print(f"平均余额: ${report['average_balance']:.2f}")
        print(f"总交易数: {report['total_transactions']}")
        print(f"高价值账户: {report['high_value_accounts']}")
        print("=" * 50)
