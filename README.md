CGTR: Convolution Graph Topology Representation for Document Ranking
Yuanyuan Qi, Jiayue Zhang, Songyan Liu, Weiran Xu and Jun Guo. CGTR: Convolution Graph Topology Representation for Document Ranking. CIKM 2020 (short).

Paper at: link?

In this paper, we take the advantage of Graph Convolutional Networks (GCN) to model global word-relation structure of a document to improve context-aware
document ranking.

If you use this work, please cite as: bibtex
????

Getting started
This code is tested on Python 3.6. Install dependencies using the following command:

pip install -r requirements.txt
You will need to prepare files for training and evaluation. Many of these files are available in data/mq2007 (LETOR4.0) and data/robust (TREC Robust 2004).

qrels: a standard TREC-style query relevant file. Used for identifying relevant items for training pair generation and for validation (data/wt/qrels, data/robust/qrels).

train_pairs: a tab-deliminted file containing pairs used for training. The training process will only use query-document pairs found in this file. Samples are in data/{wt,robust}/*.pairs. File format:

[query_id]	[doc_id]
valid_run: a standard TREC-style run file for re-ranking items for validation. The .run files used for re-ranking are available in data/{wt,robust}/*.run. Note that these runs are using the default parameters, so they do not match the tuned results shown in Table 1.

datafiles: Files containing the text of queries and documents needed for training, validation, or testing. Should be in tab-delimited format as follows, where [type] is either query or doc, [id] is the identifer of the query or document (e.g., 132, clueweb12-0206wb-59-32292), and [text] is the textual content of the query or document (no tabs or newline characters, tokenization done by BertTokenizer).

[type]  [id]  [text]
Queries for WebTrack and Robust are available in data/wt/queries.tsv and data/robust/queries.tsv. Document text can be extracted from an index using extract_docs_from_index.py (be sure to use an index that has appropriate pre-processing). The script supports both Indri and Lucene (via Anserini) indices. See instructions below for help installing pyndri or Anserini.

Examples:

# Indri index
awk '{print $3}' data/robust/*.run | python extract_docs_from_index.py indri PATH_TO_INDRI_INDEX > data/robust/documents.tsv
# Lucene index (should be built with Anserini and the -storeTransformedDocs)
awk '{print $3}' data/robust/*.run | python extract_docs_from_index.py lucene PATH_TO_LUCENE_INDEX > data/robust/documents.tsv
Running Vanilla BERT
To train a Vanilla BERT model, use the following command:

python train.py \
  --model vanilla_bert \
  --datafiles data/queries.tsv data/documents.tsv \
  --qrels data/qrels \
  --train_pairs data/train_pairs \
  --valid_run data/valid_run \
  --model_out_dir models/vbert
You can see the performance of Vanilla BERT by re-ranking a test run:

python rerank.py \
  --model vanilla_bert \
  --datafiles data/queries.tsv data/documents.tsv \
  --run data/test_run \
  --model_weights models/vbert/weights.p \
  --out_path models/vbert/test.run
Running CEDR
To train a CEDR model, first train a Vanilla BERT model, and then use the following command:

python train.py \
  --model cedr_pacrr \ # or cedr_knrm / cedr_drmm
  --datafiles data/queries.tsv data/documents.tsv \
  --qrels data/qrels \
  --train_pairs data/train_pairs \
  --valid_run data/valid_run \
  --initial_bert_weights models/vbert/weights.p \
  --model_out_dir models/cedrpacrr
You can see the performance of CEDR by re-ranking a test run:

python rerank.py \
  --model cedr_pacrr \ # or cedr_knrm / cedr_drmm
  --datafiles data/queries.tsv data/documents.tsv \
  --run data/test_run \
  --model_weights models/cedrpacrr/weights.p \
  --out_path models/cedrpacrr/test.run
Note that this will calculate results using bin/trec_eval with P@20, whereas the nDCG@20 and ERR@20 results in Table 1 are calculated using bin/gdeval.pl.
