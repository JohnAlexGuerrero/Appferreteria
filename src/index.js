var createError = require('http-errors');
const express = require('express');
const path = require('path');
const morgan = require('morgan');

//routers - rutas
const indexRouter = require('./routes/index');

const app = express();

app.set('port',4000);
app.set('view engine','ejs');
app.set('views',path.join(__dirname,'views'));

//middlewares
app.use(morgan('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false}));
app.use(express.static(path.join(__dirname, 'public')));

//rutas
app.use('/',indexRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});

app.use(function(err,req,res,next){
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err:{};

    res.status(err.status || 500);
    res.render('error');

})

module.exports = app;