# json-replacer
> Substitute the placeholder {{name}} in a JSON file with the corresponding value from another JSON {"name": "Lorenzo"}

input: `{"greet": "hello {{name}}"}`

tokens: `{"name": "Lorenzo"}`

output: `{"greet": "hello Lorenzo"}`

# 🚀 Installation
- Install it running `pip install json-replacer` in your command prompt
- Import it in your project `from json_replacer import json_replacer`
- Enjoy the package :)

# 📚 Usage 
`json_replacer()` returns a python dict (or list)

If you want to save the output as a JSON file, you have to provide the 3rd paramter `output_filename`

Check `test/test.py` for example usages

---

This project is still working in progress! There are a lot of things to implement ;)

This software is released under the [MIT license](https://github.com/lorenzua02/json-replacer/blob/main/LICENSE). Feel free to browse through the code as you like,
and if you end up making any improvements or changes, please do not hesitate to make a pull request

The project was inspired by Patryk's javascript replacer [here](https://www.npmjs.com/package/@ptkdev/json-token-replace)
