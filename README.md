<h2>LLM-ProductCard-Generator</h2>
<br>
<div>
<b>This project provides a CLI service that allows users to:</b>
<ul>
<li>Generate business-style product cards based on JSON object descriptions using an LLM.</li>
<li>Handle multiple users and API-related exceptions.</li>
<li>Create professionally formatted output for SEO.</li>
</ul>
</div>
<hr>

<div>
<h3>Local Installation on Windows</h3>
<hr>

Open a terminal and run the following commands:

```bash
git clone https://github.com/735Andrew/LLM-ProductCard-Generator
cd LLM-ProductCard-Generator 
python -m venv venv 
venv\Scripts\activate
(venv) pip install -r requirements.txt
```

Create a <b>.env</b> file in the root directory with the following variable:

```commandline 
LLM_API_TOKEN = <YOUR_API_TOKEN>
```
This project uses <b>Atria</b> as its LLM provider. <br>
You can obtain an API token here: :link:`https://api.atria‑asi.ai/docs`:link:

<br>
Open a terminal in the root directory and execute this command:

```bash
# Test input with mock data.
(venv) python main.py -p "{\"name\":\"Манометр показывающий DM 02\",\"manufacturer\":\"Манотомь\",\"specs\":{\"диапазон измерений\":\"0–1,6 МПа\",\"класс точности\":\"1,5\",\"присоединение\":\"G1/2\",\"диаметр корпуса\":\"100 мм\"},\"description\":\"Прибор предназначен для измерения избыточного давления.\"}"

# The LLM generates a structured response in the following format:
('{
"seo_title": "...",
"seo_description": "...",
"key_specifications": "...",
"search_queries": "...",
"commercial_summary": "...",
}')
```
</div>
<hr>