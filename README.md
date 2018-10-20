# speech2code
An application that generates code based on speech. Currently only supports English to Python.

## Contributors

- [Amlaan Bhoi](https://abhoi.github.io/)
- [Shubadra Govindan](https://www.linkedin.com/in/shubadra-govindan)
- [Sandeep Joshi](https://sandeepjoshi1910.github.io/)
- [Debojit Kaushik](https://dkaushik94.github.io/)

```
graph TB
    text2code-->|5|Luis_API
    speech2text-->|2|speech2text_API
    text2speech-->|A1|text2speech_API
    speech2text-->|4|text2code
    text2code-->|7|rabbitmq
    text2speech-->|A3|electron_application
    subgraph backend
    text2code
    speech2text
    text2speech
    speech_recognizer-->|1|speech2text
    end
    subgraph google
    speech2text_API
    text2speech_API
    end
    rabbitmq-->|8|electron_application
    subgraph message-broker
    rabbitmq
    end
    electron_application-->|0|speech_recognizer
    subgraph frontend
    electron_application
    end
    Luis_API-->|6|text2code
    subgraph microsoft
    Luis_API
    end
    speech2text_API-->|3|speech2text
    text2speech_API-->|A2|text2speech
```
