// Main JavaScript functionality for DailyLeet

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initLazyLoading();
    initSmoothScrolling();
    initAnimations();
    initCopyFunctionality();
    initThemeTransitions();
});

// Lazy loading for images
function initLazyLoading() {
    const images = document.querySelectorAll('img[loading="lazy"]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Animation on scroll
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);
    
    // Observe elements that should animate
    document.querySelectorAll('.glass-effect, .hover-lift').forEach(el => {
        animationObserver.observe(el);
    });
    
    // Animate skill bars
    const skillBars = document.querySelectorAll('.skill-bar');
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animationPlayState = 'running';
            }
        });
    }, observerOptions);
    
    skillBars.forEach(bar => {
        bar.style.animationPlayState = 'paused';
        skillObserver.observe(bar);
    });
}

// Copy functionality
function initCopyFunctionality() {
    // Add copy buttons to code blocks
    document.querySelectorAll('pre code').forEach(codeBlock => {
        const pre = codeBlock.parentElement;
        if (!pre.querySelector('.copy-button')) {
            const copyButton = document.createElement('button');
            copyButton.className = 'copy-button absolute top-4 right-4 text-gray-400 hover:text-white transition-colors p-2 rounded bg-black bg-opacity-50';
            copyButton.innerHTML = '<i class="fas fa-copy"></i>';
            copyButton.addEventListener('click', () => copyCodeToClipboard(codeBlock));
            
            pre.style.position = 'relative';
            pre.appendChild(copyButton);
        }
    });
}

// Copy code to clipboard
function copyCodeToClipboard(codeBlock) {
    const text = codeBlock.textContent;
    navigator.clipboard.writeText(text).then(() => {
        showToast('Code copied to clipboard!', 'success');
    }).catch(err => {
        console.error('Failed to copy code:', err);
        showToast('Failed to copy code', 'error');
    });
}

// Show toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 px-4 py-2 rounded-lg shadow-lg transform translate-y-full transition-transform duration-300 z-50 ${
        type === 'success' ? 'bg-green-500 text-white' :
        type === 'error' ? 'bg-red-500 text-white' :
        'bg-blue-500 text-white'
    }`;
    toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check' : type === 'error' ? 'times' : 'info'} mr-2"></i>${message}`;
    
    document.body.appendChild(toast);
    
    // Show toast
    setTimeout(() => {
        toast.classList.remove('translate-y-full');
    }, 100);
    
    // Hide toast
    setTimeout(() => {
        toast.classList.add('translate-y-full');
        setTimeout(() => {
            document.body.removeChild(toast);
        }, 300);
    }, 3000);
}

// Theme transitions
function initThemeTransitions() {
    // Add smooth transitions to theme-related elements
    const elements = document.querySelectorAll('.glass-effect, .hover-lift, .btn-primary');
    elements.forEach(el => {
        el.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
    });
}

// Utility functions
const utils = {
    // Debounce function for performance
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Check if element is in viewport
    isInViewport: function(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    },
    
    // Format numbers with commas
    formatNumber: function(num) {
        return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
};

// Mobile menu functionality
const mobileMenuButton = document.getElementById('mobile-menu-button');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', function(e) {
        e.stopPropagation();
        mobileMenu.classList.toggle('hidden');
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
            mobileMenu.classList.add('hidden');
        }
    });
    
    // Close mobile menu on window resize
    window.addEventListener('resize', utils.debounce(() => {
        if (window.innerWidth >= 768) {
            mobileMenu.classList.add('hidden');
        }
    }, 250));
}

// Keyboard navigation improvements
document.addEventListener('keydown', function(e) {
    // Close mobile menu on Escape
    if (e.key === 'Escape' && mobileMenu && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
    }
});

// Performance monitoring (development only)
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    window.addEventListener('load', function() {
        if ('performance' in window) {
            const loadTime = Math.round(performance.now());
            console.log(`Page loaded in ${loadTime}ms`);
        }
    });
}