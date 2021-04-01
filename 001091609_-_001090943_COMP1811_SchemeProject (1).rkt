;; hang-man for REPL Scheme

;;
(define source-name "glossary.txt")

;; Side effect:
;; Strig-> IO([String])
;; Passed the path, open the file containig glossary
(define (read-words-from glossary)
  (let* ((port (open-input-file glossary))
         (res (read-word-list port '())))
    (close-input-port port)
    res))

;; Side effect
;; Fd -> [String] -> IO ([String])
;; Passed port and acumulator, return the all the words as strings
(define (read-word-list port acc)
  (let ((stuff (read port)))
    (if (eof-object? stuff)
        acc
        (read-word-list port
                        (cons (symbol->string stuff) acc)))))

(define list-of-words (read-words-from source-name))

;; STATE OF THE GAME
(define glossary (map string->list list-of-words))
(define word-to-guess (list-ref glossary (random (length list-of-words))))
(define partial-sol (string->list (make-string (length word-to-guess) #\*)))
(define hits 0)
(define plays 0)
(define failures 0)
(define total-failures 6)
(define total-hits (length word-to-guess))

;; 
;; IO(String)
(define (game-status)
  (begin
    (format "~a H:~a/~a F:~a/~a ~a ~a"
            (list->string partial-sol)
            hits  total-hits
            failures  total-failures
            plays
            (if (and
                 (< hits total-hits)
                 (< failures total-failures))
                ""
                (string-append "GAME-OVER(" (list->string word-to-guess) ")")))))

;;;
;;  PURELY FUNCTIONAL
;;
;;F1
;; function to find the number of times a character is in a given word
(define (occurrences word char)
  (cond
    [(empty? word) 0]  ;; if list is empty
        [(equal? (first word) char)
         (+ 1 (occurrences (rest word) char))]  ;; if characters match
        [else
         (occurrences (rest word) char)]))  

;; tests inputs for the function
;;(occurrences  '(#\m #\a #\d #\a #\m) #\m)
;;(occurrences  '(#\c #\o #\r #\r #\u #\p #\t) #\o)

;; function to find the index of inputted character
(define (indices word char)
  (let loop ((word word)
             (idx 0)
             (result '()))
    (cond
          [(empty? word) result] ;; if no match returns empty
          [(equal? (first word) char)
               (set! result (append result (list idx))) ;; if match append list
          (loop (rest word) (add1 idx) result)]   
          [else (loop (rest word) (add1 idx) result)]))) ;; loops through rest of the word and adds matching characters

;; testing inputs
;;(indices '(#\d #\o #\o #\d) #\o)
;;(indices '(#\r #\e #\m  #\i #\n #\d #\e #\r) #\e)

;; function to replace matching indices with given character
(define (replace-indices word idx new)
  (if (or (null? word) (null? idx))
      word
      (let loop ((word word)
                (restlst (rest word))
                (currentrep (first word))
                (reversedlst '())          
                (idx idx)               
                (dec_idx '()))          
        (cond
          [(null? idx)
            (if (null? restlst)
                (reverse (cons currentrep reversedlst))
                (loop restlst (rest restlst) (first restlst) (cons currentrep reversedlst)
                     dec_idx '()))]
           [(zero? (first idx))
            (loop word restlst new reversedlst
                 (rest idx) dec_idx)]
           [else
            (loop word restlst currentrep reversedlst
                 (rest idx) (cons (- (first idx) 1) dec_idx))]))))

;; testing inputs
;;(replace-indices '(#\a #\ * #\ * )  '(1 2) #\b)
;;(replace-indices '(#\a #\* #\* #\* #\*)  '(0 2 4) #\b)

; function to calculate no of hits
(define (noOfHits newlst)
  (cond
    [(empty? newlst) 0]  ;; if empty it stays 0
    [(not (equal? (first newlst) #\*)) ;; not equal replaces first with *
     (+ 1 (noOfHits (rest newlst))) ]  ;; adds 1 to counter for each mathing character
    [else
     (noOfHits (rest newlst))])) ;; no match means it stays the same

;; testing inputs
;;(noOfHits '(#\m #\o #\r #\n #\i #\n #\g))
;;(noOfHits '(#\g #\o #\o #\d #\a #\y ))

;;F2
;; Side effects
;; IO(String)
(define (restart)
  (begin
    ;; some statements
    (set! word-to-guess (list-ref glossary (random (length list-of-words))))
    (set! partial-sol (string->list (make-string (length word-to-guess) #\*)))
    (set! hits 0)
    (set! plays 0)
    (set! failures 0)
    (set! total-hits (length word-to-guess))
    (set! total-failures 6)
    ;; last statement
    (game-status)))


;; Char -> IO(String)
(define (guess char)
  (begin
    ;; some statement
    (cond
      [(or (= hits total-hits) (= failures total-failures)) null]
      [else
       (begin
         ;; imcreases number of plays after each guess
         (set! plays (+ plays 1))
         ;; adds +1 to hits and shows hit on partial solution
         (if (= (occurrences partial-sol char) 0)
             (set! hits (+ hits (occurrences word-to-guess char))))
             (set! partial-sol (replace-indices partial-sol (indices word-to-guess char) char))
         ;; adds +1 to failures
             (if (= 0 (occurrences word-to-guess char))
             (set! failures (+ failures 1))))])
    ;; last statement
    (game-status)))


;; IO(String)
;; function to allow the player to make full guess
(define (solve word)
  (define answer (string->list word))
  (begin
    (for-each (lambda (char)
                (guess char)) answer)(void)))

;;
;; EXTRA -F3
;;;;;;;;;;;;;;;;;;;;;;;;;;
   
;; p: all-words as list of list of char
;; half working function that displays procedure error
;;(define (words-containing all-words char)
;; (cond
;;    (map (lambda (all-words)
;;               (if (> (words-containing all-words char) 0)
;;      [(equal? (first all-words) char)
;;      (+ 1 (words-containing (rest all-words) char))]
;;        [else
;;         (words-containing (rest all-words) char)])))))


(define (words-containing all-words char)
  (define list-of-list-of-char '())
   (map (lambda (all-words)
               (if (> (occurrences all-words char) 0)
                 (set! list-of-list-of-char
(append list-of-list-of-char(list all-words)))))all-words)list-of-list-of-char)

;; test inputs
;(words-containing '((#\b #\u #\s)(#\b #\a #\r)(#\c #\a #\r))#\b)

;; p: all-words as list of list of char
;;  : chars as a list of char
(define (words-containing-ext all-words chars) null)

;; both function under here are attempts at F3 function 2
;; both functions are working, but not as requested

;; function to display all words as a list of characters
(define list-of-list-of-char list-of-words) 
(define (func list-of-list-of-char)
  (if (empty? (cdr list-of-list-of-char))
      (display (car list-of-list-of-char))
      (begin
        (if (eq? (car list-of-list-of-char) (car (cdr list-of-list-of-char)))
            (begin
              (display (car list-of-list-of-char)))
            (display (car list-of-list-of-char)))
        (func (cdr list-of-list-of-char)))))

;; function to display glossary as unified words in a character list
(define (func glossary)
  (if (empty? (cdr glossary))
      (display (car glossary))
      (begin
        (if (eq? (car glossary) (car (cdr glossary)))
            (begin
              (display (car glossary)))
            (display (car glossary)))
        (func (cdr glossary)))))


;; IO([String])
;; this is very hard.
;; we found the previous statement to be quite accurate.
(define (sieve chars) (void))

