def split_list(data, data_size):
    batches = [data[i:i+data_size] for i in range(0, len(data), data_size)]
    return batches

# 创建一个长度为500的列表
data = list(range(0, 500))

# 定义批次大小80
data_size = 80

# 将列表拆分成多个批次
batches = split_list(data, data_size)

# 打印输出每个批次
for i, batch in enumerate(batches):
    print(f"Batch {i+1}: {batch}")