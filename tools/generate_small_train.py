# import pickle
 
# # 定义文件路径
# train_file_path = '/home/robot/Documents/cjy/bev/DifFUSER/data/nuscenes/nuscenes_infos_train.pkl'
 
# # 加载训练集数据
# print("Loading train_data")
# with open(train_file_path, 'rb') as f_train:
#     train_data = pickle.load(f_train)
 
# # 检查 train_data 的结构，统计 'prev' 的数量
# print("Counting 'lidar_path'")
# prev_count = 0
 
# # 遍历 train_data，统计包含 'prev' 键的项
# for key, value in train_data.items():
#     if isinstance(value, list):  # 确保 value 是列表
#         for item in value:
#             if isinstance(item, dict) and 'lidar_path' in item:  # 检查是否包含 'lidar_path'
#                 prev_count += 1
 
# print(f"The total count of 'lidar_path' is: {prev_count}")


import pickle
 
# 定义文件路径
input_file_path = './data/nuscenes/nuscenes_infos_train_w_3occ.pkl'
output_file_path = './data/nuscenes/nuscenes_infos_train_w_3occ_6000.pkl'
 
# 要保存的帧数
frame = 6000
 
# 加载原始数据
print("Loading data")
with open(input_file_path, 'rb') as f:
    data = pickle.load(f)
 
# 创建一个新的字典存储前 frame 帧数据
new_data = {key: [] for key in data.keys()}  # 初始化与原始数据结构一致的空字典
new_data['metadata'] = data.get('metadata', None)  # 保留原始的 'metadata' 值
prev_count = 0  # 记录已经提取的帧数
 
# 遍历原始数据，取出前 frame 帧数据
print(f"Extracting the first {frame} frames")
for key, value in data.items():
    if key == 'metadata':  # 跳过 'metadata' 键
        continue
    if isinstance(value, list):  # 确保值是列表
        for item in value:
            if isinstance(item, dict) and 'lidar_path' in item:  # 确保每个元素是字典并且含有 'lidar_path'
                new_data[key].append(item)  # 添加到新的字典中
                prev_count += 1
                if prev_count >= frame:  # 达到 frame 帧就停止
                    break
        if prev_count >= frame:  # 检查是否已收集到 frame 帧
            break
 
# 保存新的数据到文件
print(f"Saving the first {frame} frames to {output_file_path}")
with open(output_file_path, 'wb') as f_out:
    pickle.dump(new_data, f_out)
 
print(f"Completed. Saved {prev_count} frames to {output_file_path}")