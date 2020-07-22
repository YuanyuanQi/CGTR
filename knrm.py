import os

'''os.environ["CUDA_VISIBLE_DEVICES"] = "1,0"
for item in [1,2,3,4,5]:
	os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.stem.sw.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm/base-clean-stem-sw/f{2}".format(item,item,item))
	os.system("python seq_train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs.150new  --valid_run data/robust/f{1}.valid.run.150new  --model_out_dir models/robust/seq-vbert-cedr-knrm/width-27-1-res150/f{2}".format(item,item,item))
	print ('DONE',item)#'''


'''os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
for item in [3]:
	os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp800.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm/textrank-stp800-doc512-lr0.001/f{2}  --lr 0.001".format(item,item,item))
	print ('DONE',item)

	os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp800.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm/textrank-stp800-doc512-lr0.0001/f{2}  --lr 0.0001  --epoch 150".format(item,item,item))
	print ('DONE',item)#'''

#document.textrank
'''# os.environ["CUDA_VISIBLE_DEVICES"] = "1,0"
# for item in [3]:
	# os.system("python train.py  --model cedr_conv_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp1000.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-12kn-256hd-knrm-float16/textrank-stp1000-doc1000-lr0.00002/f{2}  --lr 0.00002  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model cedr_conv_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp1000.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-12kn-256hd-knrm-float16/textrank-stp1000-doc1000-lr0.00003/f{2}  --lr 0.00003  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model cedr_conv_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp1000.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-12kn-256hd-knrm-float16/textrank-stp1000-doc1000-lr0.00004/f{2}  --lr 0.00004  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model cedr_conv_knrm --datafiles data/robust/queries.tsv data/robust/documents.textrank.stp1000.Maxlen1759.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-12kn-256hd-knrm-float16/textrank-stp1000-doc1000-lr0.00005/f{2}  --lr 0.00005  --epoch 150".format(item,item,item))
	# print ('DONE',item)#'''

	
	
#robust04 document
'''# os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
# for item in [3]:
	# os.system("python train.py  --model bert_knrm_bk --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/fine-tuning/bert-knrm-orig-float16/orig-doc1200-lr0.00005/f{2}  --lr 0.00005  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm-float16/orig-doc800-lr0.00001/f{2}  --lr 0.00001  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model cedr_conv_gcn_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-gcn-knrm-float16/orig-doc1600-lr0.0001-lastlayer-bn/f{2}  --lr 0.00001  --epoch 200".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm-float16/orig-doc1200-lr0.001-13layers/f{2}  --lr 0.001  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-knrm-float16/orig-doc1200-lr0.00001-13layers/f{2}  --lr 0.00001  --epoch 250".format(item,item,item))


	# os.system("python train.py  --model cedr_gan_sim --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-gan-sim-float16/orig-doc600-lr0.0001/f{2}  --lr 0.0001  --epoch 150".format(item,item,item))
	# print ('DONE',item)

	# os.system("python train.py  --model cedr_conv_gan_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-gan-knrm-float16/orig-doc600-lr0.000001/f{2}  --lr 0.000001  --epoch 150".format(item,item,item))
	# print ('DONE',item)#'''

	# os.system("python train.py  --model cedr_conv_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv13-knrm-float16/orig-doc1200-lr0.00005/f{2}  --lr 0.00005  --epoch 250".format(item,item,item))
	# print ('DONE',item)
	
	# os.system("python train.py  --model cedr_conv_gcn_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/cedr-conv-gcn-knrm-float16-test/orig-doc1200-lr0.00005-lastlayer/f{2}  --lr 0.00005  --epoch 250".format(item,item,item))
	# print ('DONE',item)


#robust04
# os.environ["CUDA_VISIBLE_DEVICES"] = "1,0"
# for item in [3]:
	# os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/fine-tuning/bert-knrm-float16/orig-doc1200-lr0.001-lastlayer-f1/f{2}  --lr 0.001  --epoch 150".format(item,item,item))
	# print ('DONE',item)


os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
for item in [3]:
	os.system("python train.py  --model bert_knrm --datafiles data/robust/queries.tsv data/robust/documents.tsv  --qrels data/robust/qrels  --train_pairs data/robust/f{0}.train.pairs  --valid_run data/robust/f{1}.valid.run  --model_out_dir models/robust/fine-tuning/bert-knrm-float16/orig-doc1200-lr0.01-lastlayer-f1/f{2}  --lr 0.01  --epoch 150".format(item,item,item))
	print ('DONE',item)
