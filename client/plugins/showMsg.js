import Swal from 'sweetalert2'

export default ({ app }, inject) => {
    inject("showMsg", (msg = "Проверьте данные", type="error") => {
        Swal.fire({
            position: 'center',
            icon: type,
            title: msg,
            showConfirmButton: false,
            timer: 3000
        })
    });
};
