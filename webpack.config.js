
var path=require("path");
var webpack = require('webpack');
//var BundleTracker = require('webpack-bundle-tracker');



module.exports = {
    devtool: 'inline-source-map',
    context: __dirname,
    entry: path.resolve( __dirname,"/vuepy.py"),
    mode:"development",//"development","production"
    output:{"path":path.resolve( __dirname,"dist"),
            "filename": "vuepy.js"},
   module:{
   	rules: [
            {
                test: /\.py$/,
                loader: 'transcrypt-loader',
            
               
            }
        ],
   },
    resolve: {

        alias: {
            
            "Root":path.resolve( __dirname,"apps"),
            "System":path.resolve( __dirname),
            'vue': 'vue/dist/vue.esm.js',

        }
    },



}