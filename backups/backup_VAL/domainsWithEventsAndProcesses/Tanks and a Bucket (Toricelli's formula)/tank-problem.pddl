(define (problem tank-problem)
(:domain tank-domain)
(:objects tank1 tank2 bucket)
(:init (= (volume bucket) 0)
	(= (capacity bucket) 60)
	(= (volume tank1) 100)
	(= (sqrtvolinit tank1) 10)
	(= (flow-constant tank1) 0.8)
	(= (volume tank2) 64)
	(= (sqrtvolinit tank2) 8)
	(= (flow-constant tank2) 1))
(:goal (> (volume bucket) (- (capacity bucket) 2)))
(:metric minimize (total-time))) 