/**
 * Created by dongmengyuan on 19-4-12.
 */
function confirm() {
    var name = document.getElementById('username');
    var pass = document.getElementById('password');
    console.log(name);
    if (name.value === '' || pass.value === '') {
        // document.getElementById("alert").innerHTML = ('用户名、密码不能为空');
        return false;
    }
    if (name.value != 'hah' || pass.value != '123123') {
        document.getElementById("alert").innerHTML = ('用户名或密码错误');
        return false;
    }
    else {
        return true;
    }
}