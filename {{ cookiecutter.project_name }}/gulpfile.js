const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create()
var spawn = require('child_process').spawn

function style() {
    return gulp.src('{{ cookiecutter.app_name }}/static/scss/main.scss')
    .pipe(sass())
    .pipe(gulp.dest('{{ cookiecutter.app_name }}/static/css'))
    .pipe(browserSync.stream());
};

function watch() {
    browserSync.init({
        proxy: 'localhost:8000'
        });
    gulp.watch('{{ cookiecutter.app_name }}/static/scss/**/*', style);
    gulp.watch('{{ cookiecutter.app_name }}/**/*.html').on('change', browserSync.reload)
    gulp.watch('{{ cookiecutter.app_name }}/**/*.js').on('change', browserSync.reload)

}

function run_django() {
    var inst = spawn('python', ['manage.py', 'runserver', '--noreload'])

    inst.stdout.on('data', (data) => {
        console.log(`${data}`);
    });

    inst.stderr.on('data', (data) => {
        console.log(`${data}`);
    });

    return inst;

};

exports.style = style;
exports.watch = watch;
exports.run_django = run_django;

exports.default = function() {
    run_django();
    watch();
}