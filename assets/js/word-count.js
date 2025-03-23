document.addEventListener('DOMContentLoaded', function() {
    // 获取文章内容元素（适配 Jekyll 生成的页面）
    const articleContent = document.querySelector('.markdown-body');
    
    if (articleContent) {
        // 计算总字数（排除代码块和特殊标签）
        const text = articleContent.innerText.trim().replace(/\s+/g, '');
        const wordCount = text.length;
        console.log('wordCount', wordCount);
        
        // 估算阅读时间（假设普通读者每分钟阅读250个字）
        const readingTime = Math.max(1, Math.ceil(wordCount / 250));
        
        // 更新页面上的统计信息
        const wordCountElement = document.getElementById('word-count');
        const readingTimeElement = document.getElementById('reading-time');
        
        if (wordCountElement) {
            wordCountElement.textContent = wordCount;
        }
        
        if (readingTimeElement) {
            readingTimeElement.textContent = readingTime;
        }
    }
});
