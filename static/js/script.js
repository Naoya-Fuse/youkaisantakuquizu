const form = document.querySelector('form');
const checkButton = document.querySelector('#check');
const resultMessage = document.querySelector('#result-message');
const answer = document.querySelector('#answer');

checkButton.addEventListener('click', (event) => {
    event.preventDefault();
    const inputAnswer = answer.value;
    const correctAnswer = document.querySelector('answer').textContent;
    if (inputAnswer === correctAnswer) {
        resultMessage.textContent = '正解！';
        const image_name = correctAnswer + '.jpg';
        const image_path = 'input_folder/' + image_name;
        document.querySelector('#monster-image').setAttribute('src', image_path);
    } else {
        resultMessage.textContent = '不正解！正解は「' + correctAnswer + '」です。';
    }
});

