
my dataset
   
   修改数据格式为COCO，VOC等
   1:初始化类别数量参数 
     src/lib/datasets/utils/opts.py 
       def init(self, args=''):
   
   2:初始化类别名称参数 
     src/lib/datasets/utils/debugger.py 
       coco_class_name = ['traffic']

   3：coco数据集处理
     /src/lib/datasets/dataset/coco.py
	class COCO(data.Dataset):
	  #0721 
	  num_classes = 10













   1：主要目录
   2：coco_class_name： path：CenterNet/src/lib/utils/debugger.py
      类别，类别数目
    
   
    #self.parser.add_argument('--debug', type=int, default=0,
    #                         help='level of visualization.'
    #                              '1: only show the final detection results'
    #                              '2: show the network output features'
    #                              '3: use matplot to display' # useful when lunching training with ipython notebook
    #                              '4: save all visualizations to disk')
    # model
    #self.parser.add_argument('--arch', default='dla_34', 
    #                         help='model architecture. Currently tested'
    #                              'res_18 | res_101 | resdcn_18 | resdcn_101 |'
    #                              'dlav0_34 | dla_34 | hourglass')



测试阶段

   代码debugger.py 保存图像
