# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-inflect
Epoch: 100
Version: 7.5.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
License: MIT
URL: https://github.com/jaraco/inflect/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Correctly generate plurals, singular nouns, ordinals, indefinite
articles; convert numbers to words.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-inflect
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
Requires: python3
Requires: python3-more-itertools >= 8.5.0
Requires: python3-typeguard >= 4.0.1
Requires: python3-typing-extensions
Provides: python3-inflect = %{epoch}:%{version}-%{release}
Provides: python3dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(inflect) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-inflect
Correctly generate plurals, singular nouns, ordinals, indefinite
articles; convert numbers to words.

%files -n python%{python3_version_nodots}-inflect
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-inflect
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
Requires: python3
Requires: python3-more-itertools >= 8.5.0
Requires: python3-typeguard >= 4.0.1
Requires: python3-typing-extensions
Provides: python3-inflect = %{epoch}:%{version}-%{release}
Provides: python3dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(inflect) = %{epoch}:%{version}-%{release}

%description -n python3-inflect
Correctly generate plurals, singular nouns, ordinals, indefinite
articles; convert numbers to words.

%files -n python3-inflect
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-inflect
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
Requires: python3
Requires: python3-more-itertools >= 8.5.0
Requires: python3-typeguard >= 4.0.1
Requires: python3-typing-extensions
Provides: python3-inflect = %{epoch}:%{version}-%{release}
Provides: python3dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(inflect) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-inflect = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(inflect) = %{epoch}:%{version}-%{release}

%description -n python3-inflect
Correctly generate plurals, singular nouns, ordinals, indefinite
articles; convert numbers to words.

%files -n python3-inflect
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
