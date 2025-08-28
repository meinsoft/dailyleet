# Claude Code Instructions for DailyLeet

## Project Overview
DailyLeet is a minimalist Django website for sharing LeetCode solutions and coding tutorials. The design emphasizes elegance, professionalism, and clean aesthetics with a black, white, and deep blue color palette.

## Development Setup

### Installation Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Linting and Code Quality
```bash
# Format code (if black is installed)
black .

# Check for issues (if flake8 is installed)
flake8 .
```

## Architecture

### Apps Structure
- **core**: Homepage and main views
- **videos**: YouTube video management and display
- **blog**: Markdown blog system
- **about**: Profile and personal information

### Key Models
- **Video**: YouTube videos with code, tags, difficulty
- **Post**: Blog posts with Markdown content
- **Profile**: Personal information and experience
- **Tag/Category**: Organization and filtering

### URL Structure
- `/`: Homepage with hero and featured content
- `/videos/`: Video listing with filtering
- `/videos/<slug>/`: Individual video pages
- `/blog/`: Blog post listing
- `/blog/<slug>/`: Individual blog posts
- `/about/`: Profile and story page
- `/admin/`: Django admin with Jazzmin theme

## Design Philosophy

### Color Palette
- **Primary**: Deep blue (#1e40af, #3b82f6)
- **Background**: Black (#000000)
- **Surface**: Deep blue (#0f172a), Navy (#1e293b)
- **Text**: White, gray variants (#e2e8f0, #cbd5e1, #94a3b8)

### Typography
- **Display**: Poppins (headings, logo)
- **Body**: Inter (general text)
- **Code**: JetBrains Mono (code blocks)

### Components
- **Glass Effects**: Subtle transparency with backdrop blur
- **Hover Animations**: Smooth lift effects and color transitions
- **Cards**: Rounded corners, proper spacing, visual hierarchy
- **Buttons**: Gradient backgrounds with hover states

## Content Management

### Adding Videos
1. Admin → Videos → Add Video
2. Paste YouTube URL (ID extracted automatically)
3. Set difficulty, tags, and code snippet
4. Thumbnail generated automatically

### Writing Blog Posts
1. Admin → Blog → Posts → Add Post
2. Write in Markdown format
3. HTML generated automatically with syntax highlighting
4. Reading time calculated automatically

### Profile Updates
1. Admin → About → Profile
2. Update bio, skills, experience
3. Upload images and resume files

## Performance Considerations
- Lazy loading for images
- Optimized database queries with select_related/prefetch_related
- Proper indexing on frequently queried fields
- CDN for static assets (Tailwind, fonts, icons)

## Security Features
- CSRF protection enabled
- Secure headers configuration
- Admin panel secured and not exposed publicly
- Input sanitization and validation
- Proper user permissions

## Responsive Design
- Mobile-first approach
- Tailwind CSS breakpoints (sm, md, lg, xl)
- Flexible grid systems
- Touch-friendly interface elements
- Optimized for all screen sizes

## SEO Optimization
- Semantic HTML structure
- Meta descriptions and titles
- Open Graph tags ready
- Clean URL structure
- Proper heading hierarchy

## Development Notes
- Follow Django best practices
- Keep design minimalist and elegant
- Maintain consistent spacing and typography
- Test responsive behavior on all devices
- Ensure accessibility with proper ARIA labels

## Common Tasks

### Adding New Features
1. Create models in appropriate app
2. Add admin configuration
3. Create views and URL patterns  
4. Design templates following existing patterns
5. Test responsive behavior

### Styling Guidelines
- Use Tailwind utility classes
- Maintain glass effect consistency
- Follow established color palette
- Keep animations subtle and purposeful
- Ensure proper contrast ratios

### Code Quality
- Use meaningful variable names
- Add docstrings to complex functions
- Follow PEP 8 style guidelines
- Keep views simple, move logic to models
- Use Django's built-in features when possible