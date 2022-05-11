from flask import Flask, request, json, jsonify, abort


app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    content_type = request.headers.get("Content-Type")
    if (content_type == "application/json"):
        data = request.json
        cut_str = StringCut(data["string_to_cut"])
        json_str = {"return_string": cut_str}
    else:
        return "Content-Type not be supported"
    return jsonify(json_str)

def StringCut(string):
    i = 0
    cut_str_list = []
    for char in string:
        i += 1
        if i == 3:
            cut_str_list.append(char)
            i = 0
    final_cut_str = "".join(cut_str_list)
    return final_cut_str

if __name__ == "__main__":
	app.run(debug = True)
