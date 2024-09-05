<!-- WEASEL: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 Weasel Project: Asking Questions to Confucius in Classical Chinese Texts

This project uses annotated data from Classical Chinese works to train a part of speech tagger and named entity recognizer. We construct an NLP pipeline that can isolate sentences in Classical texts where a named person is asking a question to Confucius. Texts are taken from the Kanseki Repository.


## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[Weasel documentation](https://github.com/explosion/weasel).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install-dependencies` | Install python dependencies |
| `install-language` | Install the language module from Cadet |
| `convert-raw-text` | Convert raw text files to spaCy's format |
| `convert-annotations` | Convert annotated data from INCEpTION to spaCy's format |
| `split-data` | Split the data into training, validation, and test sets |
| `debug-data` | Validate the training data |
| `debug-config` | Validate the selected spaCy config file |
| `pretrain-model` | Pretrain context for the language model |
| `train-model` | Train the language model |
| `evaluate-model` | Evaluate the model using test data and save the metrics |
| `package-model` | Package the trained model so it can be installed |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`weasel run [name]`](https://github.com/explosion/weasel/tree/main/docs/cli.md#rocket-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `install-dependencies` &rarr; `install-language` &rarr; `convert-raw-text` &rarr; `convert-annotations` &rarr; `split-data` &rarr; `debug-data` &rarr; `debug-config` &rarr; `pretrain-model` &rarr; `train-model` |
| `install` | `install-dependencies` &rarr; `install-language` |
| `setup` | `convert-raw-text` &rarr; `convert-annotations` &rarr; `split-data` &rarr; `debug-data` |
| `train` | `debug-config` &rarr; `pretrain-model` &rarr; `train-model` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`weasel assets`](https://github.com/explosion/weasel/tree/main/docs/cli.md#open_file_folder-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/lang/lzh`](assets/lang/lzh) | Local | New language module from Cadet |
| [`assets/text`](assets/text) | Local | Raw text files for pretraining |
| [`assets/annotations`](assets/annotations) | Local | Annotated text files from INCEpTION |

<!-- WEASEL: AUTO-GENERATED DOCS END (do not remove) -->
