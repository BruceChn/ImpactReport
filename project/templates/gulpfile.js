var gulp = require('gulp');
var gultil = require('gulp-util');
var source = require('vinyl-source-stream');
var browserify = require('browserify');
var watchify = require('watchify');
var babelify = require('babelify');


gulp.task('overview',function(){
	var bundler = watchify(browserify({
		entries:['./src/overview.jsx'],
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
			.pipe(source('overview.js'))
			.pipe(gulp.dest('../static/js'));

	}
	build();
	bundler.on('update',build);
});

gulp.task('progress',function(){
	var bundler = watchify(browserify({
		entries:['./src/progress.jsx'],
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
			.pipe(source('progress.js'))
			.pipe(gulp.dest('../static/js'));

	}
	build();
	bundler.on('update',build);
});
gulp.task('report',function(){
	var bundler = watchify(browserify({
		entries:['./src/report.jsx'],
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
			.pipe(source('report.js'))
			.pipe(gulp.dest('../static/js'));

	}
	build();
	bundler.on('update',build);
});

gulp.task('default',['overview','progress','report']);
