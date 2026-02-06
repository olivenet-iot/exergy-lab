import { useState } from 'react';
import { Copy, FileDown, Check } from 'lucide-react';

const AIActionBar = ({ contentRef, fileName = 'ai-yorum' }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    if (!contentRef?.current) return;
    const text = contentRef.current.innerText || contentRef.current.textContent;
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Fallback for older browsers
      const textarea = document.createElement('textarea');
      textarea.value = text;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const handlePDF = () => {
    if (!contentRef?.current) return;
    const printWindow = window.open('', '_blank');
    if (!printWindow) return;

    printWindow.document.write(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>ExergyLab - AI Yorum Raporu</title>
        <style>
          body { font-family: 'Segoe UI', system-ui, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #1f2937; }
          h1, h2, h3 { color: #111827; }
          .header { border-bottom: 2px solid #0891b2; padding-bottom: 12px; margin-bottom: 24px; }
          .header h1 { font-size: 20px; margin: 0; }
          .header p { font-size: 12px; color: #6b7280; margin: 4px 0 0 0; }
          table { width: 100%; border-collapse: collapse; margin: 8px 0; }
          td, th { border: 1px solid #e5e7eb; padding: 6px 10px; text-align: left; font-size: 13px; }
          th { background: #f9fafb; }
        </style>
      </head>
      <body>
        <div class="header">
          <h1>ExergyLab - AI Analiz Raporu</h1>
          <p>${new Date().toLocaleDateString('tr-TR', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' })}</p>
        </div>
        ${contentRef.current.innerHTML}
      </body>
      </html>
    `);
    printWindow.document.close();
    printWindow.focus();
    setTimeout(() => {
      printWindow.print();
    }, 250);
  };

  return (
    <div className="flex items-center gap-2">
      <button
        onClick={handleCopy}
        className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
        title="Panoya kopyala"
      >
        {copied ? (
          <>
            <Check className="w-3.5 h-3.5 text-green-600" />
            <span className="text-green-600">Kopyalandi</span>
          </>
        ) : (
          <>
            <Copy className="w-3.5 h-3.5" />
            Kopyala
          </>
        )}
      </button>
      <button
        onClick={handlePDF}
        className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-gray-600 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors"
        title="PDF olarak indir"
      >
        <FileDown className="w-3.5 h-3.5" />
        PDF
      </button>
    </div>
  );
};

export default AIActionBar;
