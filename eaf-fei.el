;;; eaf-fei.el --- Demo  -*- lexical-binding: t; -*-

;;; Code:

;;;###autoload
(defun eaf-open-fei ()
  "Open EAF demo screen to verify that EAF is working properly."
  (interactive)
  (eaf-open "eaf-fei" "fei"))

(setq eaf-fei-module-path (concat (file-name-directory load-file-name) "buffer.py"))
(add-to-list 'eaf-app-module-path-alist '("fei" . eaf-fei-module-path))

(provide 'eaf-fei)

;;; eaf-fei.el ends here
