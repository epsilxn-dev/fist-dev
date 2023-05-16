export default ({ app }, inject) => {
    inject("toFormData", (obj, imageKey = "image") => {
        let formData = new FormData()
        for (let key of Object.keys(obj)) {
            if (Array.isArray(obj[key])) {
                for (let i in obj[key]) {
                    formData.append(`${key}[${i}]`, obj[key][i]);
                }
            } else if (key == imageKey) {
                if (obj[key])
                    formData.append(key, obj[key], obj[key].name);
            } else {
                formData.append(key, obj[key]);
            }
        }
        return formData
    });
};
