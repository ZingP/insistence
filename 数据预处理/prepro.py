import os
import sys

def load_data(file_path, limits=1000):
    """从文件加载数据"""
    data_set = set()
    count = 0
    # 需要考虑长度大于6的，小于6的
    with open(file_path, "r") as f:
        for line in f:
            li = line.split("\t")
            leng = len(li)
            if leng == 6:
                info = li[2]
            elif leng > 6:
                info = li[2]
            else:
                info = "".join(li[1:-1])
            if len(info) >=2 and info != "NULL":
                data_set.add(info)
                count += 1
                if count == limits:
                    yield data_set
                    data_set = set()
                    count = 0
    yield data_set

def clean_text_zh(text):
    """中文数据清洗"""
    # 去除空格
    text = re.sub(' ', '', text)
    # 去掉全角空白符，\u3000 是全角的空白符
    text = re.sub('\u3000', '', text)
    # 去掉 \xa0 是不间断空白符 &nbsp;
    text = re.sub('\xa0', '', text)
    # 去掉未识别的表情符号
    text = re.sub('<U+.*>', '', text)
    # 去除英文标点, 这应该放在最后
    text = text.translate(
        str.maketrans('', '', string.punctuation))
    return text

# 清除emoji
def filter_emoji(srcstr, restr=''):  
    """过滤emoji"""
    # 编译匹配表情的正则
    prog = emoji.get_emoji_regexp()
    return prog.sub(restr, srcstr) 
    
def write_file(string, file_path):
    with open(file_path, "a+", encoding="utf-8") as f:
        f.write(string)
        f.write("\n")


rootdir = "/home/datamining/liuyouyuan/online/hotevents/data/toEsData"
files = ["audio_info_20200225.tsv", 
         "audio_info_20200301.tsv", 
         "audio_info_20200302.tsv",
         "audio_info_20200303.tsv",
         "audio_info_20200304.tsv",
         "audio_info_20200305.tsv",
         "audio_info_20200306.tsv"]

if __name__ == "__main__":
    data_file = "./info.txt"
    for file_ in files:
        file_path = os.path.join(rootdir, file_)
        data_set = load_data(file_path)
        n = 0
        for set_obj in data_set:
            for s in set_obj:
                try:
                    write_file(s, data_file)
                except Exception as e:
                    print(s, e)
            n += 1
            if n==5:
                print("退出")
                sys.exit(-1)