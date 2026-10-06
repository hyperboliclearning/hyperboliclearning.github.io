const copyCitationButton = document.querySelector('.copy-citation');
const citationCode = document.getElementById('citation-code');
const copyStatus = document.querySelector('.copy-status');

if (copyCitationButton && citationCode && copyStatus) {
  let resetTimer;
  const buttonLabel = copyCitationButton.querySelector('span');

  copyCitationButton.addEventListener('click', async () => {
    clearTimeout(resetTimer);
    const text = citationCode.textContent.trim() + '\n';
    let copied = false;

    try {
      await navigator.clipboard.writeText(text);
      copied = true;
    } catch {
      // Older browsers can copy from a temporary selection during the click.
      const field = document.createElement('textarea');
      field.value = text;
      field.setAttribute('readonly', '');
      field.style.cssText = 'position:fixed;left:-9999px;top:0;';
      document.body.appendChild(field);
      field.select();
      try {
        copied = document.execCommand('copy');
      } catch {
        copied = false;
      } finally {
        field.remove();
        copyCitationButton.focus({ preventScroll: true });
      }
    }

    if (copied) {
      buttonLabel.textContent = 'Copied!';
      copyStatus.textContent = 'BibTeX copied to clipboard.';
    } else {
      const range = document.createRange();
      range.selectNodeContents(citationCode);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      buttonLabel.textContent = 'Copy';
      copyStatus.textContent = 'Citation selected. Press Ctrl+C or Command+C to copy.';
    }

    resetTimer = setTimeout(() => {
      buttonLabel.textContent = 'Copy';
      copyStatus.textContent = '';
    }, 4000);
  });
}
