import sys
sys.path.append('../')  # 添加自定义库的目录
from pycore.tikzeng import *  #  导入自定义库

# defined your arch
arch = [
    # 添加头
    to_head( '..' ),
    to_cor(),
    to_begin(),
    # 添加卷积层conv1
    to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2, caption="conv1"),
    # 卷积层conv1东侧添加池化层pool1
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", caption="pool1"),
    # 池化层pool1东侧添加卷积层conv2
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2, caption="conv2"),
    # 建立pool1到conv2的连接箭头
    to_connection( "pool1", "conv2"), 
    # conv2东侧添加pool2
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1, caption="pool2"),
    # pool1东侧添加softmax层但是偏移３单位
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="softmax"),
    # 建立pool2到soft1的连接箭头
    to_connection("pool2", "soft1"),    
    # 结束
    to_end()
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )


if __name__ == '__main__':
    main()
