const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const PORT = 4000

app.get('/', (req, res) =>
    res.json(
        process.env.WELCOM_MESSAGE ?
            `${process.env.WELCOM_MESSAGE}` :
            "Hello, no WELCOME MESSAGE!"
    )
);
app.get('/api', (req, res) => {
    res.send({
        "courses": [
            "PHP",
            "VueJS",
            "Laravel",
            "Node"
        ]
    });
});
app.get('/random', (req, res) =>
    res.json(
        Math.random()
    )
);
app.listen(PORT,()=>console.log(`on port ${PORT}`))