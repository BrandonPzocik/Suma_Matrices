const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(path.join(__dirname, "public")));

app.post("/sumar", (req, res) => {
    const { matriz1, matriz2 } = req.body;
    if (!Array.isArray(matriz1) || !Array.isArray(matriz2)) {
        return res.status(400).json({ error: "Datos inválidos" });
    }
    const resultado = matriz1.map((fila, i) => 
        fila.map((num, j) => (Number(num) || 0) + (Number(matriz2[i][j]) || 0))
    );
    res.json({ resultado });
});

app.listen(3000, () => console.log("Servidor en http://localhost:3000"));