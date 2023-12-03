// تعيين النهاية (endpoint) للـ API
const endpoint = 'https://vidsrc.to/vapi/movie/';

// دالة لجلب البيانات من الـ API
async function fetchMovies(type, page) {
    try {
        const response = await fetch(`${endpoint}${type}/${page}`);
        const data = await response.json();
        return data; // البيانات المسترجعة من الـ API
    } catch (error) {
        console.error('حدث خطأ: ', error);
        return null;
    }
}

// استخدام الدالة لجلب الأفلام الشهيرة (مثال)
fetchMovies('popular', 1)
    .then(data => {
        // عمل شيء مع البيانات المسترجعة
        console.log('البيانات: ', data);
    })
    .catch(error => {
        console.error('حدث خطأ: ', error);
    });
