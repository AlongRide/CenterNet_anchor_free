
cd src

# office test
#python demo.py ctdet --demo ../data/test_drving/007015.jpg \
#--load_model ../exp/ctdet/coco_resdcn101/model_best.pth \
#--arch resdcn_101

#python demo.py ctdet --demo ../images/007119.jpg \
#--load_model ../exp/ctdet/coco_dla_1x/model_best.pth


python main.py ctdet --exp_id coco_dla_2x --batch_size 4 \
--master_batch 4 --lr 5e-6 --gpus 0 --num_workers 4 \
--num_epochs 300 --lr_step 150,180


# train  coco_dla_1x
#python main.py ctdet --exp_id coco_dla_1x --batch_size 2 --master_batch 2 \
#--lr 5e-6 --gpus 0 --num_workers 4 \
#--dataset coco


#python main.py ctdet --exp_id coco_resdcn101 \
#--arch resdcn_101 --batch_size 2 --master_batch 4 \
#--lr 3.75e-6 --gpus 0 --num_workers 4


#python main.py ctdet --exp_id coco_hg --arch hourglass \
#--batch_size 1 --master_batch 4 --lr 2.5e-6 \
#--gpus 0


# train resdcn_18
#python main.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 \
#--batch_size 4 --master_batch 4 --lr 5e-4 --gpus 0 --num_workers 16 \
#--dataset coco


# test
#python test.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 --keep_res --resume
# flip test
#python test.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 --keep_res --resume --flip_test 
# multi scale test
#python test.py ctdet --exp_id coco_resdcn18 --arch resdcn_18 --keep_res --resume --flip_test --test_scales 0.5,0.75,1,1.25,1.5
#cd ..
