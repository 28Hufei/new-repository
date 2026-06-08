"""
银行账户模型
"""

class Account:
    """
    代表一个银行账户
    """
    
    def __init__(self, account_id, account_holder, balance=0.0, account_type="Savings"):
        """
        初始化账户
        
        Args:
            account_id: 账户ID
            account_holder: 账户持有人
            balance: 初始余额
            account_type: 账户类型 (Savings/Checking/Investment)
        """
        self.account_id = account_id
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
        self.transactions = []
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                'type': 'deposit',
                'amount': amount,
                'balance_after': self.balance
            })
            return True
        return False
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append({
                'type': 'withdraw',
                'amount': amount,
                'balance_after': self.balance
            })
            return True
        return False
    
    def get_balance(self):
        """获取账户余额"""
        return self.balance
    
    def get_transactions(self):
        """获取交易历史"""
        return self.transactions
