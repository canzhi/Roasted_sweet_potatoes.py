class SweetPotato:
    """定义了一个地瓜类"""

    def __init__(self):
        # 地瓜4种状态
        self.roasted_state = "生的"
        # 总共烤了多久
        self.roasted_spend_time = 0
        # 添加佐料列表
        self.condiments = []

    def __str__(self):
        sep="/"
        str=sep.join(self.condiments)
        return "地瓜的状态,添加的佐料有:%s,烤了%d分钟：%s" % (str, self.roasted_spend_time, self.roasted_state)

    # 定义了一个方法，烤地瓜
    def roast(self, roasted_time):  # 接受一个额外的参数，说明又烤了多久地瓜
        self.roasted_spend_time = self.roasted_spend_time + roasted_time
        st = self.roasted_spend_time
        if st >= 0 and st < 3:
            self.roasted_state = "生的"
        elif st >= 3 and st < 5:
            self.roasted_state = "半生不熟"
        elif st >= 5 and st < 8:
            self.roasted_state = "熟了"
        elif st >= 8:
            self.roasted_state = "烤糊了"

    def add_condiments(self, condiment):
        self.condiments.append(condiment)


sp = SweetPotato()
# 开始烤地瓜
sp.roast(1)  # 给烤地瓜的方法传入一个参数，烤了多久（分钟）
print(sp)
sp.roast(1)
print(sp)
sp.roast(1)
print(sp)
sp.add_condiments("大蒜")
sp.roast(1)
print(sp)
sp.roast(1)
print(sp)
sp.add_condiments("番茄酱")
sp.roast(1)
print(sp)
sp.roast(1)
print(sp)
sp.add_condiments("孜然")
sp.roast(1)
print(sp)
sp.add_condiments("芥末")
sp.roast(1)
print(sp)
sp.roast(1)
print(sp)
