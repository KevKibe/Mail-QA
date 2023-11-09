import React, { useEffect, useRef, useState } from 'react';


const ScrollAnimation = ({ animation, duration, delay, offset, children }) => {
  const elementRef = useRef(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const element = elementRef.current;
      if (!element) return;

      const rect = element.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      const shouldAnimate = rect.top - windowHeight + offset <= 0;

      if (shouldAnimate) {
        setIsVisible(true);
        element.style.animation = `${animation} ${duration}ms ${delay}ms both`;
      }
    };

    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [animation, duration, delay, offset]);

  return (
    <div ref={elementRef} className={`scroll-animation ${isVisible ? 'visible' : ''}`}>
      {children}
    </div>
  );
};

export default ScrollAnimation;
