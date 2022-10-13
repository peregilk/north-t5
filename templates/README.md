---
language: 
- no
- nn
- sv
- dk
- is
- en

datasets:
- nbailab/NCC
- mc4
- wikipedia


widget:
- text: <extra_id_0> hver uke samles Regjeringens medlemmer til Statsråd på <extra_id_1>. Dette organet er øverste <extra_id_2> i Norge. For at møtet skal være <extra_id_3>, må over halvparten av regjeringens <extra_id_4> være til stede.
- text: På <extra_id_0> kan man <extra_id_1> en bok, og man kan også <extra_id_2> seg ned og lese den.

license: apache-2.0
---

The North-T5-models are a set of Norwegian sequence-to-sequence-models. It builds upon the flexible [T5](https://github.com/google-research/text-to-text-transfer-transformer) and [T5X](https://github.com/google-research/t5x) and can be used for a variety of NLP tasks ranging from classification to translation.

##MODELS##

## Performance
A thorough evaluation of the North-T5 models is planned, and I strongly recommend external researchers to make their own evaluation. The main advantage with the T5-models are their flexibility. Traditionally, encoder-only models (like BERT) excels in classification tasks, while seq-2-seq models are easier to train for tasks like translation and Q&A. Despite this, here are the results from using North-T5 on the political classification task explained [here](https://arxiv.org/abs/2104.09617). 

|**Model:** | **F1** |
|:-----------|:------------|
|mT5-base|73.2 |
|mBERT-base|78.4 |
|NorBERT-base|78.2 |
|North-T5-small|80.5 |
|nb-bert-base|81.8 |
|North-T5-base|85.3 |
|North-T5-large|86.7 |
|North-T5-xl|88.7 |
|North-T5-xxl|91.8|

These are preliminary results. The [results](https://arxiv.org/abs/2104.09617) from the BERT-models are based on the test-results from the best model after 10 runs with early stopping and a decaying learning rate. The T5-results are the average of five runs on the evaluation set. The small-model was trained for 10.000 steps, while the rest for 5.000 steps. A fixed learning rate was used (no decay), and no early stopping. Neither was the recommended rank classification used. We use a max sequence length of 512. This method simplifies the test setup and gives results that are easy to interpret. However, the results from the T5 model might actually be a bit sub-optimal.  

## Sub-versions of North-T5
The following sub-versions are available. More versions will be available shorter.

|**Model** | **Description** |
|:-----------|:-------|
|**North&#8209;T5&#8209;NCC** |This is the main version. It is trained an additonal 500.000 steps on from the mT5 checkpoint. The training corpus is based on [the Norwegian Colossal Corpus (NCC)](https://huggingface.co/datasets/NbAiLab/NCC). In addition there are added data from MC4 and English Wikipedia.| 
|**North&#8209;T5&#8209;NCC&#8209;lm**|The model is pretrained for an addtional 100k steps on the LM objective discussed in the [T5 paper](https://arxiv.org/pdf/1910.10683.pdf). In a way this turns a masked language model into an autoregressive model. It also prepares the model for some tasks. When for instance  doing translation and NLI, it is well documented that there is a clear benefit to do a step of unsupervised LM-training before starting the finetuning.| 
##PRIV-DESC##

## Fine-tuned versions
As explained below, the model really needs to be fine-tuned for specific tasks. This procedure is relatively simple, and the models are not very sensitive to the hyper-parameters used. Usually a decent result can be obtained by using a fixed learning rate of 1e-3. Smaller versions of the model typically needs to be trained for a longer time. It is easy to train the base-models in a Google Colab.

Since some people really want to see what the models are capable of, without going through the training procedure, I provide a couple of test models. These models are by no means optimised, and are just for demonstrating how the North-T5 models can be used.

* Nynorsk Translator. Translates any text from Norwegian Bokmål to Norwegian Nynorsk. Please test the [Streamlit-demo](https://huggingface.co/spaces/north/Nynorsk) and the [HuggingFace repo](https://huggingface.co/north/demo-nynorsk-base)
* DeUnCaser. The model adds punctation, spaces and capitalisation back into the text. The input needs to be in Norwegian but does not have to be divided into sentences or have proper capitalisation of words. You can even remove the spaces from the text, and make the model reconstruct it. It can be tested with the [Streamlit-demo](https://huggingface.co/spaces/north/DeUnCaser) and directly on the [HuggingFace repo](https://huggingface.co/north/demo-deuncaser-base)


## Training details
All models are built using the Flax-based T5X codebase, and all models are initiated with the mT5 pretrained weights. The models are trained using the T5.1.1 training regime, where they are only trained on an unsupervised masking-task. This also means that the models (contrary to the original T5) needs to be finetuned to solve specific tasks. This finetuning is however usually not very compute intensive, and in most cases it can be performed even with free online training resources.

All the main model model versions are trained for 500.000 steps after the mT5 checkpoint (1.000.000 steps). They are trained mainly on a 75GB corpus, consisting of NCC, Common Crawl and some additional high quality English text (Wikipedia). The corpus is roughly 80% Norwegian text. Additional languages are added to retain some of the multilingual capabilities, making the model both more robust to new words/concepts and also more suited as a basis for translation tasks.

While the huge models almost always will give the best results, they are also both more difficult and more expensive to finetune. I will strongly recommended to start with finetuning a base-models. The base-models can easily be finetuned on a standard graphic card or a free TPU through Google Colab.  

All models were trained on TPUs. The largest XXL model was trained on a TPU v4-64, the XL model on a TPU v4-32, the Large model on a TPU v4-16 and the rest on TPU v4-8. Since it is possible to reduce the batch size during fine-tuning, it is also possible to finetune on slightly smaller hardware. The rule of thumb is that you can go "one step down" when finetuning. The large models still rewuire access to significant hardware, even for finetuning.

## Formats
All models are trained using the Flax-based T5X library. The original checkpoints are available in T5X format and can be used for both finetuning or interference. All models, except the XXL-model, are also converted to Transformers/HuggingFace. In this framework, the models can be loaded for finetuning or inference both in Flax, PyTorch and TensorFlow format.

## Future
I will continue to train and release additional models to this set. What models that are added is dependent upon the feedbacki from the users

## Thanks
This release would not have been possible without getting support and hardware from the [TPU Research Cloud](https://sites.research.google/trc/about/) at Google Research. Both the TPU Research Cloud Team and the T5X Team has provided extremely useful support for getting this running. 

Freddy Wetjen at the National Library of Norway has been of tremendous help in generating the original NCC corpus, and has also contributed to generate the collated coprus used for this training. In addition he has been a dicussion partner in the creation of these models. 

Also thanks to Stefan Schweter for writing the [script](https://github.com/huggingface/transformers/blob/main/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py)  for converting these models from T5X to HuggingFace and to Javier de la Rosa for writing the dataloader for reading the HuggingFace Datasets in T5X.

## Warranty
Use at your own risk. The models have not yet been thougroughly tested, and may contain both errors and biases.

## Contact/About
These models were trained by Per E Kummervold. Please contact me on per@capia.no.
