var gulp = require('gulp');
var gultil = require('gulp-util');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var watchify = require('watchify');
var babelify = require('babelify');


gulp.task('default',function(){
	var bundler = watchify(browserify({
		entries:['./src/app.jsx'],
		transform:[['babelify',{presets:["react"]}]],
		extensions:['.jsx'],
		debug : true,
		cache:{},
		packageCache:{},
		fullPaths:true
	}));

	function build(file){
		if(file) gultil.log('Recompiling ' + file);
		return bundler
			.bundle()
			.on('error',gultil.log.bind(gultil,'Browserify Error'))
			.pipe(source('main.js'))
			.pipe(gulp.dest('../static/js'));

	}
	build();
	bundler.on('update',build);
});
