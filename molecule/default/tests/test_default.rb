# frozen_string_literal: true

describe command('/opt/node/bin/node --version') do
  its('stdout') { should eq "v8.11.3\n" }
end

describe command('node --version') do
  its('stdout') { should eq "v8.11.3\n" }
end

describe command('/opt/node/bin/npm --version') do
  its('stdout') { should eq "5.6.0\n" }
end

describe command('npm --version') do
  its('stdout') { should eq "5.6.0\n" }
end

describe command('/opt/node/bin/npx --version') do
  its('stdout') { should eq "9.7.1\n" }
end

describe command('npx --version') do
  its('stdout') { should eq "9.7.1\n" }
end
