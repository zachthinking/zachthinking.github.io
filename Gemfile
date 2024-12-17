source "https://mirrors.tuna.tsinghua.edu.cn/rubygems"

gem "github-pages", group: :jekyll_plugins
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-analytics"
  gem "rouge"
  gem "wdm", ">= 0.1.0" if Gem.win_platform?
end

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end
