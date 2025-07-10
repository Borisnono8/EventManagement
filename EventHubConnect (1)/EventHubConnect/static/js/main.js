// Main JavaScript file for Event Management System

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize datetime inputs
    initializeDatetimeInputs();
    
    // Initialize search functionality
    initializeSearch();
    
    // Initialize confirmation dialogs
    initializeConfirmationDialogs();
    
    // Initialize auto-hide alerts
    initializeAlerts();
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
    
    // Initialize loading states
    initializeLoadingStates();
});

// Initialize Bootstrap tooltips
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Form validation enhancements
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Real-time validation
    const inputs = document.querySelectorAll('.form-control, .form-select');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(this);
        });
        
        input.addEventListener('input', function() {
            if (this.classList.contains('is-invalid')) {
                validateField(this);
            }
        });
    });
}

// Validate individual field
function validateField(field) {
    if (field.checkValidity()) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
    }
}

// Initialize datetime inputs with default values
function initializeDatetimeInputs() {
    const startDateInput = document.getElementById('start_datetime');
    const endDateInput = document.getElementById('end_datetime');
    
    if (startDateInput && !startDateInput.value) {
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        tomorrow.setHours(10, 0, 0, 0);
        startDateInput.value = formatDateTimeLocal(tomorrow);
    }
    
    if (endDateInput && !endDateInput.value) {
        const dayAfterTomorrow = new Date();
        dayAfterTomorrow.setDate(dayAfterTomorrow.getDate() + 1);
        dayAfterTomorrow.setHours(17, 0, 0, 0);
        endDateInput.value = formatDateTimeLocal(dayAfterTomorrow);
    }
    
    // Auto-update end date when start date changes
    if (startDateInput && endDateInput) {
        startDateInput.addEventListener('change', function() {
            const startDate = new Date(this.value);
            const endDate = new Date(endDateInput.value);
            
            if (endDate <= startDate) {
                const newEndDate = new Date(startDate);
                newEndDate.setHours(newEndDate.getHours() + 2);
                endDateInput.value = formatDateTimeLocal(newEndDate);
            }
        });
    }
}

// Format date for datetime-local input
function formatDateTimeLocal(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    
    return `${year}-${month}-${day}T${hours}:${minutes}`;
}

// Initialize search functionality
function initializeSearch() {
    const searchForm = document.querySelector('form[method="GET"]');
    if (searchForm) {
        const searchInput = searchForm.querySelector('input[name="search"]');
        if (searchInput) {
            searchInput.addEventListener('input', debounce(function() {
                if (this.value.length >= 3 || this.value.length === 0) {
                    // Auto-submit search after 500ms delay
                    setTimeout(() => {
                        searchForm.submit();
                    }, 500);
                }
            }, 300));
        }
    }
}

// Debounce function for search
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Initialize confirmation dialogs
function initializeConfirmationDialogs() {
    const deleteButtons = document.querySelectorAll('[data-confirm]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const message = this.getAttribute('data-confirm') || 'Are you sure?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
}

// Initialize auto-hide alerts
function initializeAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        // Auto-hide success and info alerts after 5 seconds
        if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });
}

// Initialize smooth scrolling
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Initialize loading states
function initializeLoadingStates() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                const originalText = submitButton.innerHTML;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
                
                // Re-enable button after 10 seconds as fallback
                setTimeout(() => {
                    submitButton.disabled = false;
                    submitButton.innerHTML = originalText;
                }, 10000);
            }
        });
    });
}

// Utility functions
const Utils = {
    // Format date for display
    formatDate: function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    // Format datetime for display
    formatDateTime: function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    },
    
    // Show toast notification
    showToast: function(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white bg-${type} border-0`;
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;
        
        const toastContainer = document.getElementById('toast-container') || createToastContainer();
        toastContainer.appendChild(toast);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Remove toast element after it's hidden
        toast.addEventListener('hidden.bs.toast', function() {
            this.remove();
        });
    },
    
    // Copy text to clipboard
    copyToClipboard: function(text) {
        navigator.clipboard.writeText(text).then(() => {
            this.showToast('Copied to clipboard!', 'success');
        }).catch(() => {
            this.showToast('Failed to copy to clipboard', 'danger');
        });
    }
};

// Create toast container if it doesn't exist
function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// Event handlers for dynamic content
function handleRegistrationToggle(eventId, isRegistered) {
    const button = document.querySelector(`[data-event-id="${eventId}"]`);
    if (!button) return;
    
    const url = isRegistered ? 
        `/events/${eventId}/unregister` : 
        `/events/${eventId}/register`;
    
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCsrfToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            location.reload();
        } else {
            Utils.showToast(data.message || 'An error occurred', 'danger');
        }
    })
    .catch(error => {
        Utils.showToast('An error occurred', 'danger');
    });
}

// Get CSRF token from meta tag or form
function getCsrfToken() {
    const metaTag = document.querySelector('meta[name="csrf-token"]');
    if (metaTag) {
        return metaTag.getAttribute('content');
    }
    
    const tokenInput = document.querySelector('input[name="csrf_token"]');
    if (tokenInput) {
        return tokenInput.value;
    }
    
    return '';
}

// Print functionality
function printPage() {
    window.print();
}

// Export event attendees (placeholder for future implementation)
function exportAttendees(eventId, format = 'csv') {
    Utils.showToast('Export functionality coming soon!', 'info');
}

// Global error handler
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Don't show error toast for now to avoid spam
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(function() {
            const perf = performance.getEntriesByType('navigation')[0];
            if (perf.loadEventEnd - perf.navigationStart > 3000) {
                console.warn('Page loaded slowly:', perf.loadEventEnd - perf.navigationStart + 'ms');
            }
        }, 0);
    });
}
