# Nord-T5
The Nord-T5 is a set of Norwegian seq-2-seq-models for doing Norwegian NLP. It builds upon the flexible T5 text-to-text platform and can be used for a variety of NLP tasks ranging from classification to translation.

The models are built using the Flax-based T5X codebase, and all models are initiated with the mT5 pretrained weights. The models are trained using the T5.1.1 training regime, where the only task they are only trained on an unsupervised masking-task. This also means that the models (contrary to the original T5) needs to be finetuned to solve specific tasks. This finetuning is however usually not very compute intensive, and in most cases it can be performed even with free online training resources.

## Main versions
|**Model:** | **Parameters** |
|:-----------|:------------|
|Nord-T5-small|60 million |
|Nord-T5-base|220 million |
|Nord-T5-large|770 million |
|Nord-T5-xl|3 billion |
|Nord-T5-xxl|11 billion|


## Sub-versions of Nord-T5-Base
|**Model:** | **Description** |
|:-----------|:------------|
|Nord-byT5-base | A vocabulary free version of T5. Trained exactly like NordT5, but instead of the 200.000 vocabulary, this model ..... This model might be of particulary interest for tasks involving for instance spelling correction, OCR-cleaning, handwriting recognition etc. However, it will, by design, have a shorter maximum sequence length.|
|Nord-T5-base-LM |Pretrained for an addtional 100k steps on the LM objective described in Raffel & al. In a way this turns a masked language model into an autoregressive model. It also prepares the model for some tasks. When for instance  doing translation and NLI, it is well documented that there is a clear benefit to do a step of unsupervised LM-training before starting the finetuning.| 
|Nord-T5-base-modern | Pretrained for an additional 200k steps on a blanaced Bokmål and Nynorsk corpus. While original made for doing translation between Bokmål and Nynorsk, it might also give improved results on tasks where you know that the input/output is modern "standard" text. A significant part of the training corpus is newspapers and reports.|
|Nord-T5-base-scandinavian |Pretrained for an additional 200k steps on a corpus with the Scandinavian languages (Bokmål, Nynorsk, Danish, Swedish and Icelandic (+ a tiny bit Faeroyish)). The model was trained for increasing the understanding of what effect such training has on various languages.|


## Training details
All the main model model versions are trained for 500.000 steps after the mT5 checkpoint (1.000.000 steps). They are all trained mainly on a 75GB corpus, consisting of NCC, Common Crawl and some additional high quality English text (Wikipedia). The corpus is roughly 80% Norwegian text. Additional languages are added to retain some of the multilingual capabilities, making the model both more robust to new words/concepts and also more suited as a basis for translation tasks.

While the huge models almost always will give the best results, they are also both difficult and expensive to finetune. It is strongly recommended to start with finetuning on a base-models. This can typically easily be finetuned on a standard graphic card or a free TPU through Google Colab. The sub-versions of the Nord-T5-base model was created with this in mind. 

All models were trained on TPUs. The largest XXL model was trained on a TPU v4-64, the XL model on a TPU v4-16, and the rest on TPU v4-8.

## Formats
The models are trained using the T5X library, and the original checkpoints are available. The T5X library is also well suited for doing additional finetuning or interference. The models is also converted to Transformers/HuggingFace. In this framework, the models are available both in Flax, PyTorch and TensorFlow format.

## Future
I will continue to train and release additional models based on this framework. Contact me directly if you need other specific version for research projects.

## Contact/About
These models were trained by Per E Kummervold. Please contact me on per@capia.no.

## Thanks
This release would not have been possible without getting support from [TPU Research Cloud](https://sites.research.google/trc/about/) at Google Research. 
NB
NCC
Freddy


