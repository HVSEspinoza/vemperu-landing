from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

# CATÁLOGO COMPLETO CON PRECIOS PSICOLÓGICOS
PRODUCTS = [
    {
        "id": "office2021",
        "name": "Microsoft Office Professional Plus 2021",
        "price": 79,
        "old_price": 599,
        "highlight": False,
        "features": ["Word, Excel, PowerPoint, Outlook, Access", "Activación permanente", "Para 1 PC"]
    },
    {
        "id": "office365-trial",
        "name": "Office 365 Prueba 1 Año",
        "price": 99,
        "old_price": 199,
        "highlight": False,
        "features": ["Acceso completo a todas las apps", "1TB OneDrive incluido", "Prueba por 1 año"]
    },
    {
        "id": "windows11",
        "name": "Windows 11 Pro",
        "price": 79,
        "old_price": 499,
        "highlight": True,
        "features": ["Activación permanente", "Actualizaciones de por vida", "Compatibilidad total"]
    },
    {
        "id": "autodesk",
        "name": "Autodesk Collection 2025 (AutoCAD + Revit + más)",
        "price": 199,
        "old_price": 9500,
        "highlight": False,
        "features": ["Suite completa profesional", "Activación con tu correo", "1 año completo"]
    },
    {
        "id": "office2024",
        "name": "Microsoft Office LTSC Professional Plus 2024",
        "price": 89,
        "old_price": 699,
        "highlight": False,
        "features": ["Versión empresarial 2024", "Licencia permanente", "Para 1 PC"]
    },
    {
        "id": "coreldraw",
        "name": "CorelDRAW Technical Suite",
        "price": 49,
        "old_price": 399,
        "highlight": False,
        "features": ["Diseño técnico profesional", "Todas las herramientas", "1 año completo"]
    },
    {
        "id": "sketchup",
        "name": "SketchUp Pro",
        "price": 89,
        "old_price": 1200,
        "highlight": False,
        "features": ["Modelado 3D profesional", "Licencia permanente", "Extensiones incluidas"]
    },
    {
        "id": "adobe",
        "name": "Adobe Creative Cloud 2025 (IA Generativa)",
        "price": 449,
        "old_price": 2200,
        "highlight": False,
        "features": ["Photoshop, Illustrator, Premiere + Firefly IA", "Todas las apps", "1 año completo"]
    },
    {
        "id": "eset",
        "name": "ESET NOD32 Antivirus",
        "price": 29,
        "old_price": 149,
        "highlight": False,
        "features": ["Protección esencial", "1 dispositivo", "1 año completo"]
    },
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)