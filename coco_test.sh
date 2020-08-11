
cd src

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

# office
#python demo.py ctdet --demo /home/zyt/torch_tensorflow/py3torch/train_image/ \
#--load_model /home/zyt/torch_tensorflow/py3torch/CenterNet/models/ctdet_coco_dla_2x.pth


       # resdcn_101       
# single img
#python demo.py ctdet --demo ../data/test_drving/009943.jpg \
#--load_model ../exp/ctdet/coco_resdcn101/model_last.pth \
#--arch resdcn_101 --debug 4 
# test
#python test.py ctdet --exp_id coco_resdcn101 --keep_res --resume --arch resdcn_101
# flip test
#python test.py ctdet --exp_id coco_resdcn101 --keep_res --resume --flip_test --arch resdcn_101

# ctdet_coco_dla_2x.pth    all test image
python demo.py ctdet --demo /home/zyt/torch_tensorflow/py3torch/CenterNet/test_light/ \
--load_model /home/zyt/torch_tensorflow/py3torch/CenterNet/exp/ctdet/coco_dla_2x/model_best.pth
#--input_h 640 --input_w 640
       # coco_dla_2x       
# single img
#python demo.py ctdet --demo ../data/test_drving/009957.jpg \
#--load_model ../exp/ctdet/coco_dla_2x/model_last.pth \
#--arch dla_34 --debug 4 
# test
#python test.py ctdet --exp_id coco_dla_2x --keep_res --resume --arch dla_2x
# flip test
#python test.py ctdet --exp_id coco_dla_2x --keep_res --resume --flip_test --arch dla_2x



       # coco_dla_1x       
# single img
#python demo.py ctdet --demo ../data/test_drving/007331.jpg \
#--load_model ../exp/ctdet/coco_dla_1x/model_last.pth \
#--arch dla_34 --debug 4 
# test
#python test.py ctdet --exp_id coco_dla_2x --keep_res --resume --arch dla_2x
# flip test
#python test.py ctdet --exp_id coco_dla_2x --keep_res --resume --flip_test --arch dla_2x