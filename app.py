from bs4 import BeautifulSoup
from flask import Flask, abort, render_template, request
from requests import get

app = Flask(__name__)


@app.route("/", methods=["GET"])
def router():
    try:
        book = request.args.get("book", "")
        index = request.args.get("index", "")
        response = get(f"http://www.shengxuxu.net/{book}/read_{index}.html", timeout=10)
        html = response.content.decode("utf-8")
        bs = BeautifulSoup(html, "html.parser")
        title = bs.select_one("h1 a").get_text(strip=True)
        div = bs.find("div", id="chaptercontent")

        for br in div.find_all("br"):
            br.replace_with("\n")

        content = "　　" + div.get_text("\n　　", strip=True)
        forward = f"/?book={book}&index={int(index) + 1}"
        return render_template(
            "index.html", title=title, content=content, forward=forward
        )
    except Exception:
        abort(500, description="Error")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
