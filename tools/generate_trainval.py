import pickle
 
# 加载训练集和验证集的数据
print("loading train_data")
with open('/home/robot/Documents/cjy/bev/DifFUSER/data/nuscenes/nuscenes_infos_train.pkl', 'rb') as f_train:
    train_data = pickle.load(f_train)
 
print("loading val_data")
with open('/home/robot/Documents/cjy/bev/DifFUSER/data/nuscenes/nuscenes_infos_val.pkl', 'rb') as f_val:
    val_data = pickle.load(f_val)
 
# 合并两个字典
print("merging")
for key, val in val_data.items():
    # import pdb;pdb.set_trace()
    if key in train_data:
        # 如果这个 key 的值是列表，进行列表合并
        if isinstance(train_data[key], list) and isinstance(val, list):
            train_data[key].extend(val)  # 合并列表
            print("merged")
    else:
        train_data[key] = val  # 如果 train_data 中没有这个 key，直接添加
 
# 保存为新的合并文件
print("saving")
with open('/home/robot/Documents/cjy/bev/DifFUSER/data/nuscenes/nuscenes_infos_trainval.pkl', 'wb') as f_merged:
    pickle.dump(train_data, f_merged)
 
print("done")