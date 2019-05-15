module.exports = (app) => {
    app.get('/', (req, res) => {
        res.render('index.html');
    });
    app.get('/and', (req, res) => {
        res.render('and.html');
    })
}