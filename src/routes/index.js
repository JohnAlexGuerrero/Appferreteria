const express = require('express');
const router = express.Router();
const dashboard = require('../models/index');
/* GET home page. */


router.get('/',function (req,res,next){
  
      res.render('index');
      

});

module.exports = router;