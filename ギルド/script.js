document.getElementById('joinForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // 入力を取得
    const name = document.getElementById('name').value;
    const comment = document.getElementById('comment').value;
  
    // 簡易バリデーション
    if (name && comment) {
      document.getElementById('confirmation').classList.remove('hidden');
      this.reset(); // フォームリセット
    }
  });
  